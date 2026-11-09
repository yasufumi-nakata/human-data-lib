"""Render the public all-entry catalog page from the JSON catalog."""

from __future__ import annotations

from pathlib import Path

from human_data_lib import load_catalog


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "catalog.md"
INDEX_OUTPUT = ROOT / "docs/catalog-index.md"

SCALE_ORDER = (
    "molecular",
    "cellular",
    "tissue",
    "organ-system",
    "whole-person",
    "behavioral",
    "clinical",
    "population",
    "environmental",
    "infrastructure",
)


def main() -> None:
    catalog = load_catalog(ROOT / "src/human_data_lib/data/libraries.json")
    lines: list[str] = [
        "# 全件カタログ",
        "",
        "このページは `libraries.json` から生成した、人間由来バイオデータ解析カタログの全件表示です。JSON を直接読まなくても、公開ページ上で全項目を確認できます。",
        "",
        f"- 項目数: {len(catalog)}",
        f"- カタログ生成日: {catalog.generated_at}",
        f"- スキーマ: {catalog.schema_version}",
        "- [分野・解析スケール別索引](docs/catalog-index.md)",
        "- [出典確認・保留候補・品質点検](docs/catalog-review-2026-11-09.md)",
        "",
        "## 解析スケール別件数",
        "",
        "| Scale | Count |",
        "| --- | ---: |",
    ]

    scale_counts = catalog.facet_counts("scales")
    for scale in SCALE_ORDER:
        if scale in scale_counts:
            lines.append(f"| `{scale}` | {scale_counts[scale]} |")
    for scale, count in scale_counts.items():
        if scale not in SCALE_ORDER:
            lines.append(f"| `{_escape(scale)}` | {count} |")

    lines.extend(
        [
            "",
            "## 全項目",
            "",
            "| ID | Name | Type | Scales | Domains | Modalities | Tasks | Ecosystems | Official | Repo | License | Status / Notes | Summary |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for entry in catalog:
        lines.append(
            "| {id} | {name} | {type} | {scales} | {domains} | {modalities} | {tasks} | {ecosystems} | {official} | {repo} | {license} | {status} | {summary} |".format(
                id=f'<a id="{entry.id}"></a>`{_escape(entry.id)}`',
                name=_link(entry.name, entry.official_url),
                type=f"`{_escape(entry.artifact_type)}`",
                scales=_values(entry.scales),
                domains=_values(entry.domains),
                modalities=_values(entry.modalities),
                tasks=_values(entry.tasks),
                ecosystems=_values(entry.ecosystems),
                official=_link("公式", entry.official_url),
                repo=_link("repo", entry.repo_url),
                license=_escape(entry.license or "未確認"),
                status=_escape(" / ".join(filter(None, (entry.maturity, entry.notes)))),
                summary=_escape(entry.summary_ja),
            )
        )

    lines.extend(
        [
            "",
            "## 更新方法",
            "",
            "カタログを更新した後は、次のコマンドでこのページを再生成します。",
            "",
            "```bash",
            "make catalog-page",
            "make validate",
            "make test",
            "```",
        ]
    )
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    render_index(catalog)


def render_index(catalog) -> None:
    """Generate navigable facet indexes from the same source of truth."""
    lines = [
        "# 分野・解析スケール別索引", "",
        f"{catalog.generated_at} 時点、{len(catalog)} 件。複数タグの項目は複数箇所に現れます。", "",
        "各リンクは全件カタログの該当行に移動します。収録は推奨・性能保証・医療用途の承認を意味しません。", "",
        "- [全件カタログ](../catalog.md)",
        "- [今回の調査と未確認範囲](catalog-review-2026-11-09.md)", "",
    ]
    for field, title in (("scales", "解析スケール"), ("domains", "分野")):
        lines.extend([f"## {title}", ""])
        counts = catalog.facet_counts(field)
        for tag in sorted(counts):
            lines.append(f"- [{_escape(tag)}](#{field}-{tag.casefold()}) ({counts[tag]})")
        lines.append("")
        for tag in sorted(counts):
            lines.extend([f'<a id="{field}-{tag.casefold()}"></a>', f"### {tag} ({counts[tag]})", ""])
            entries = sorted((entry for entry in catalog if tag in getattr(entry, field)), key=lambda e: e.name.casefold())
            for entry in entries:
                status = " [archived]" if entry.maturity == "archived" else ""
                lines.append(f"- [{_escape(entry.name)}](../catalog.md#{entry.id}){status}")
            lines.append("")
    INDEX_OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _values(values: tuple[str, ...]) -> str:
    return "<br>".join(f"`{_escape(value)}`" for value in values)


def _link(label: str, url: str) -> str:
    return f"[{_escape(label)}]({url})"


def _escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


if __name__ == "__main__":
    main()
