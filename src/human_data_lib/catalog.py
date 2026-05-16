"""Catalog loading, validation, search, and export helpers."""

from __future__ import annotations

from dataclasses import dataclass
import csv
import json
from importlib import resources
from io import StringIO
from pathlib import Path
from typing import Any, Iterable, Iterator
from urllib.parse import urlparse


REQUIRED_ENTRY_FIELDS = {
    "id",
    "name",
    "artifact_type",
    "domains",
    "modalities",
    "tasks",
    "ecosystems",
    "scales",
    "official_url",
    "repo_url",
    "summary_ja",
}


class CatalogError(ValueError):
    """Raised when the bundled catalog is malformed."""


@dataclass(frozen=True)
class LibraryEntry:
    """One library, tool, workflow, format, standard, or ecosystem entry."""

    id: str
    name: str
    artifact_type: str
    domains: tuple[str, ...]
    modalities: tuple[str, ...]
    tasks: tuple[str, ...]
    ecosystems: tuple[str, ...]
    scales: tuple[str, ...]
    official_url: str
    summary_ja: str
    repo_url: str
    license: str | None = None
    maturity: str | None = None
    notes: str | None = None

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "LibraryEntry":
        missing = REQUIRED_ENTRY_FIELDS - raw.keys()
        if missing:
            missing_list = ", ".join(sorted(missing))
            raise CatalogError(f"{raw.get('id', '<unknown>')} is missing: {missing_list}")

        return cls(
            id=_as_nonempty_string(raw, "id"),
            name=_as_nonempty_string(raw, "name"),
            artifact_type=_as_nonempty_string(raw, "artifact_type"),
            domains=_as_tuple(raw, "domains"),
            modalities=_as_tuple(raw, "modalities"),
            tasks=_as_tuple(raw, "tasks"),
            ecosystems=_as_tuple(raw, "ecosystems"),
            scales=_as_tuple(raw, "scales"),
            official_url=_as_nonempty_string(raw, "official_url"),
            summary_ja=_as_nonempty_string(raw, "summary_ja"),
            repo_url=_as_nonempty_string(raw, "repo_url"),
            license=_as_optional_string(raw.get("license")),
            maturity=_as_optional_string(raw.get("maturity")),
            notes=_as_optional_string(raw.get("notes")),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "artifact_type": self.artifact_type,
            "domains": list(self.domains),
            "modalities": list(self.modalities),
            "tasks": list(self.tasks),
            "ecosystems": list(self.ecosystems),
            "scales": list(self.scales),
            "official_url": self.official_url,
            "repo_url": self.repo_url,
            "license": self.license,
            "maturity": self.maturity,
            "summary_ja": self.summary_ja,
            "notes": self.notes,
        }

    def haystack(self) -> str:
        parts: list[str] = [
            self.id,
            self.name,
            self.artifact_type,
            self.official_url,
            self.summary_ja,
            self.repo_url or "",
            self.license or "",
            self.maturity or "",
            self.notes or "",
            *self.domains,
            *self.modalities,
            *self.tasks,
            *self.ecosystems,
            *self.scales,
        ]
        return " ".join(parts).casefold()


@dataclass(frozen=True)
class Catalog:
    """Validated catalog with convenience indexes."""

    schema_version: str
    generated_at: str
    scope_note: str
    entries: tuple[LibraryEntry, ...]

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Catalog":
        if not isinstance(raw, dict):
            raise CatalogError("catalog root must be an object")

        entries_raw = raw.get("entries")
        if not isinstance(entries_raw, list) or not entries_raw:
            raise CatalogError("catalog entries must be a non-empty list")

        entries = tuple(LibraryEntry.from_dict(entry) for entry in entries_raw)
        _validate_unique_ids(entries)
        _validate_repo_urls(entries)

        return cls(
            schema_version=_root_string(raw, "schema_version"),
            generated_at=_root_string(raw, "generated_at"),
            scope_note=_root_string(raw, "scope_note"),
            entries=entries,
        )

    def __iter__(self) -> Iterator[LibraryEntry]:
        return iter(self.entries)

    def __len__(self) -> int:
        return len(self.entries)

    def get(self, entry_id: str) -> LibraryEntry:
        normalized = entry_id.casefold()
        for entry in self.entries:
            if entry.id.casefold() == normalized:
                return entry
        raise KeyError(entry_id)

    def search(
        self,
        query: str | None = None,
        *,
        domain: str | None = None,
        modality: str | None = None,
        task: str | None = None,
        ecosystem: str | None = None,
        scale: str | None = None,
        artifact_type: str | None = None,
    ) -> tuple[LibraryEntry, ...]:
        terms = [term.casefold() for term in (query or "").split() if term]

        def matches(entry: LibraryEntry) -> bool:
            if terms and not all(term in entry.haystack() for term in terms):
                return False
            if domain and not _contains(entry.domains, domain):
                return False
            if modality and not _contains(entry.modalities, modality):
                return False
            if task and not _contains(entry.tasks, task):
                return False
            if ecosystem and not _contains(entry.ecosystems, ecosystem):
                return False
            if scale and not _contains(entry.scales, scale):
                return False
            if artifact_type and entry.artifact_type.casefold() != artifact_type.casefold():
                return False
            return True

        return tuple(entry for entry in self.entries if matches(entry))

    def facet_counts(self, field: str) -> dict[str, int]:
        if field not in {
            "artifact_type",
            "domains",
            "modalities",
            "tasks",
            "ecosystems",
            "scales",
        }:
            raise CatalogError(f"unsupported facet: {field}")

        counts: dict[str, int] = {}
        for entry in self.entries:
            values = getattr(entry, field)
            if isinstance(values, str):
                values = (values,)
            for value in values:
                counts[value] = counts.get(value, 0) + 1
        return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))

    def to_json(self, entries: Iterable[LibraryEntry] | None = None) -> str:
        selected = tuple(entries) if entries is not None else self.entries
        return json.dumps(
            {
                "schema_version": self.schema_version,
                "generated_at": self.generated_at,
                "scope_note": self.scope_note,
                "entries": [entry.to_dict() for entry in selected],
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )

    def to_csv(self, entries: Iterable[LibraryEntry] | None = None) -> str:
        selected = tuple(entries) if entries is not None else self.entries
        output = StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=[
                "id",
                "name",
                "artifact_type",
                "domains",
                "modalities",
                "tasks",
                "ecosystems",
                "scales",
                "official_url",
                "repo_url",
                "license",
                "maturity",
                "summary_ja",
                "notes",
            ],
        )
        writer.writeheader()
        for entry in selected:
            row = entry.to_dict()
            for key in ("domains", "modalities", "tasks", "ecosystems", "scales"):
                row[key] = ";".join(row[key])
            writer.writerow(row)
        return output.getvalue()

    def to_markdown(self, entries: Iterable[LibraryEntry] | None = None) -> str:
        selected = tuple(entries) if entries is not None else self.entries
        lines = [
            "| ID | Name | Scales | Domains | Tasks | Ecosystems | Summary |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        for entry in selected:
            lines.append(
                "| {id} | [{name}]({url}) | {scales} | {domains} | {tasks} | {ecosystems} | {summary} |".format(
                    id=_escape_markdown(entry.id),
                    name=_escape_markdown(entry.name),
                    url=entry.official_url,
                    scales=_escape_markdown(", ".join(entry.scales)),
                    domains=_escape_markdown(", ".join(entry.domains)),
                    tasks=_escape_markdown(", ".join(entry.tasks)),
                    ecosystems=_escape_markdown(", ".join(entry.ecosystems)),
                    summary=_escape_markdown(entry.summary_ja),
                )
            )
        return "\n".join(lines) + "\n"


def load_catalog(path: str | Path | None = None) -> Catalog:
    """Load the bundled catalog, or a catalog from an explicit JSON path."""

    if path is None:
        text = resources.files("human_data_lib.data").joinpath("libraries.json").read_text(
            encoding="utf-8"
        )
    else:
        text = Path(path).read_text(encoding="utf-8")
    return Catalog.from_dict(json.loads(text))


def _as_tuple(raw: dict[str, Any], key: str) -> tuple[str, ...]:
    value = raw.get(key)
    if not isinstance(value, list) or not value:
        raise CatalogError(f"{raw.get('id', '<unknown>')}.{key} must be a non-empty list")
    result = tuple(item.strip() for item in value if isinstance(item, str) and item.strip())
    if len(result) != len(value):
        raise CatalogError(f"{raw.get('id', '<unknown>')}.{key} must contain only strings")
    return result


def _as_nonempty_string(raw: dict[str, Any], key: str) -> str:
    value = raw.get(key)
    if not isinstance(value, str) or not value.strip():
        raise CatalogError(f"{raw.get('id', '<unknown>')}.{key} must be a non-empty string")
    if key.endswith("_url") and not value.startswith(("https://", "http://")):
        raise CatalogError(f"{raw.get('id', '<unknown>')}.{key} must be an HTTP URL")
    return value.strip()


def _as_optional_string(value: Any) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise CatalogError("optional string fields must be strings when present")
    stripped = value.strip()
    return stripped or None


def _root_string(raw: dict[str, Any], key: str) -> str:
    value = raw.get(key)
    if not isinstance(value, str) or not value.strip():
        raise CatalogError(f"{key} must be a non-empty string")
    return value.strip()


def _validate_unique_ids(entries: Iterable[LibraryEntry]) -> None:
    seen: set[str] = set()
    for entry in entries:
        if entry.id in seen:
            raise CatalogError(f"duplicate id: {entry.id}")
        seen.add(entry.id)


def _validate_repo_urls(entries: Iterable[LibraryEntry]) -> None:
    for entry in entries:
        parsed = urlparse(entry.repo_url)
        path_parts = [part for part in parsed.path.split("/") if part]
        if parsed.netloc in {"github.com", "gitlab.com"} and len(path_parts) < 2:
            raise CatalogError(f"{entry.id}.repo_url must point to a repository, not an org")


def _contains(values: Iterable[str], needle: str) -> bool:
    normalized = needle.casefold()
    return any(normalized in value.casefold() for value in values)


def _escape_markdown(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")
