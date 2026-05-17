"""Render the public all-entry catalog page from the JSON catalog."""

from __future__ import annotations

from pathlib import Path

from human_data_lib import load_catalog


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "catalog.md"

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
            "| ID | Name | Type | Scales | Domains | Modalities | Tasks | Ecosystems | Official | Repo | Summary |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for entry in catalog:
        lines.append(
            "| {id} | {name} | {type} | {scales} | {domains} | {modalities} | {tasks} | {ecosystems} | {official} | {repo} | {summary} |".format(
                id=f"`{_escape(entry.id)}`",
                name=_link(entry.name, entry.official_url),
                type=f"`{_escape(entry.artifact_type)}`",
                scales=_values(entry.scales),
                domains=_values(entry.domains),
                modalities=_values(entry.modalities),
                tasks=_values(entry.tasks),
                ecosystems=_values(entry.ecosystems),
                official=_link("公式", entry.official_url),
                repo=_link("repo", entry.repo_url),
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


def _values(values: tuple[str, ...]) -> str:
    return "<br>".join(f"`{_escape(value)}`" for value in values)


def _link(label: str, url: str) -> str:
    return f"[{_escape(label)}]({url})"


def _escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


if __name__ == "__main__":
    main()
