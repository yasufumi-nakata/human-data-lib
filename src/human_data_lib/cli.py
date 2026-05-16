"""Command line interface for the human-data-lib catalog."""

from __future__ import annotations

import argparse
import sys
from typing import Sequence

from .catalog import CatalogError, LibraryEntry, load_catalog


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="human-data-lib",
        description="人間由来バイオデータ解析ライブラリ・ツールのカタログを検索します。",
    )
    parser.add_argument(
        "--catalog",
        help="既定の同梱カタログではなく、指定した JSON カタログを読み込みます。",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="カタログ項目を一覧します。")
    _add_filters(list_parser)
    list_parser.add_argument(
        "--format",
        choices=("table", "json", "csv", "markdown"),
        default="table",
        help="出力形式です。",
    )

    search_parser = subparsers.add_parser("search", help="キーワードと絞り込みで検索します。")
    search_parser.add_argument("query", nargs="*", help="検索語です。")
    _add_filters(search_parser)
    search_parser.add_argument(
        "--format",
        choices=("table", "json", "csv", "markdown"),
        default="table",
        help="出力形式です。",
    )

    show_parser = subparsers.add_parser("show", help="ID を指定して詳細を表示します。")
    show_parser.add_argument("id", help="項目 ID です。")
    show_parser.add_argument(
        "--format",
        choices=("text", "json", "markdown"),
        default="text",
        help="出力形式です。",
    )

    stats_parser = subparsers.add_parser("stats", help="件数とファセット集計を表示します。")
    stats_parser.add_argument(
        "--facet",
        choices=("artifact_type", "domains", "modalities", "tasks", "ecosystems", "scales"),
        default="domains",
        help="集計する項目です。",
    )

    validate_parser = subparsers.add_parser("validate", help="カタログのスキーマを検証します。")
    validate_parser.set_defaults(validate_only=True)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        catalog = load_catalog(args.catalog)
    except (CatalogError, OSError, ValueError) as exc:
        print(f"カタログを読み込めませんでした: {exc}", file=sys.stderr)
        return 2

    if getattr(args, "validate_only", False):
        print(f"OK: {len(catalog)} 件のカタログ項目を検証しました。")
        return 0

    if args.command == "stats":
        print(f"項目数: {len(catalog)}")
        for key, count in catalog.facet_counts(args.facet).items():
            print(f"{key}\t{count}")
        return 0

    if args.command == "show":
        try:
            entry = catalog.get(args.id)
        except KeyError:
            print(f"見つかりませんでした: {args.id}", file=sys.stderr)
            return 1
        _print_entries(catalog, (entry,), args.format)
        return 0

    if args.command == "list":
        entries = catalog.search(
            domain=args.domain,
            modality=args.modality,
            task=args.task,
            ecosystem=args.ecosystem,
            scale=args.scale,
            artifact_type=args.artifact_type,
        )
        _print_entries(catalog, entries, args.format)
        return 0

    if args.command == "search":
        query = " ".join(args.query)
        entries = catalog.search(
            query=query,
            domain=args.domain,
            modality=args.modality,
            task=args.task,
            ecosystem=args.ecosystem,
            scale=args.scale,
            artifact_type=args.artifact_type,
        )
        _print_entries(catalog, entries, args.format)
        return 0

    parser.error(f"unknown command: {args.command}")
    return 2


def _add_filters(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--domain", help="分野で絞り込みます。例: genomics, neurophysiology")
    parser.add_argument("--modality", help="データ種別で絞り込みます。例: EEG, EHR")
    parser.add_argument("--task", help="処理段階で絞り込みます。例: quality-control")
    parser.add_argument("--ecosystem", help="言語・エコシステムで絞り込みます。例: Python, R")
    parser.add_argument("--scale", help="尺度で絞り込みます。例: molecular, cellular, population")
    parser.add_argument("--artifact-type", help="library, tool, workflow, standard などで絞り込みます。")


def _print_entries(catalog, entries: Sequence[LibraryEntry], output_format: str) -> None:
    if output_format == "json":
        print(catalog.to_json(entries))
        return
    if output_format == "csv":
        print(catalog.to_csv(entries), end="")
        return
    if output_format == "markdown":
        print(catalog.to_markdown(entries), end="")
        return
    if output_format == "text":
        for entry in entries:
            print(f"{entry.name} ({entry.id})")
            print(f"  種別: {entry.artifact_type}")
            print(f"  分野: {', '.join(entry.domains)}")
            print(f"  データ: {', '.join(entry.modalities)}")
            print(f"  処理: {', '.join(entry.tasks)}")
            print(f"  環境: {', '.join(entry.ecosystems)}")
            print(f"  尺度: {', '.join(entry.scales)}")
            print(f"  公式: {entry.official_url}")
            if entry.repo_url:
                print(f"  リポジトリ: {entry.repo_url}")
            if entry.license:
                print(f"  ライセンス: {entry.license}")
            if entry.maturity:
                print(f"  成熟度: {entry.maturity}")
            print(f"  要約: {entry.summary_ja}")
            if entry.notes:
                print(f"  注記: {entry.notes}")
        return

    _print_table(entries)


def _print_table(entries: Sequence[LibraryEntry]) -> None:
    if not entries:
        print("該当する項目はありません。")
        return

    widths = {
        "id": min(max(len(entry.id) for entry in entries), 28),
        "name": min(max(len(entry.name) for entry in entries), 28),
        "scales": 30,
        "domains": 30,
        "tasks": 34,
    }
    header = (
        f"{'ID':{widths['id']}}  "
        f"{'Name':{widths['name']}}  "
        f"{'Scales':{widths['scales']}}  "
        f"{'Domains':{widths['domains']}}  "
        f"{'Tasks':{widths['tasks']}}"
    )
    print(header)
    print("-" * len(header))
    for entry in entries:
        print(
            f"{_clip(entry.id, widths['id']):{widths['id']}}  "
            f"{_clip(entry.name, widths['name']):{widths['name']}}  "
            f"{_clip(', '.join(entry.scales), widths['scales']):{widths['scales']}}  "
            f"{_clip(', '.join(entry.domains), widths['domains']):{widths['domains']}}  "
            f"{_clip(', '.join(entry.tasks), widths['tasks']):{widths['tasks']}}"
        )


def _clip(value: str, width: int) -> str:
    if len(value) <= width:
        return value
    if width <= 1:
        return value[:width]
    return value[: width - 1] + "…"


if __name__ == "__main__":
    raise SystemExit(main())
