# カタログスキーマ

カタログ本体は `src/human_data_lib/data/libraries.json` です。

## ルート

```json
{
  "schema_version": "0.1.0",
  "generated_at": "2026-05-19",
  "scope_note": "説明",
  "entries": []
}
```

## entry

必須フィールド:

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `id` | string | 安定 ID |
| `name` | string | 表示名 |
| `artifact_type` | string | library, tool, workflow, standard など |
| `domains` | string[] | 分野タグ |
| `modalities` | string[] | データ種別タグ |
| `tasks` | string[] | 処理段階タグ |
| `ecosystems` | string[] | 言語・実行環境・周辺エコシステム |
| `scales` | string[] | 解析尺度タグ |
| `official_url` | string | 公式 URL |
| `repo_url` | string | 公式または準公式の公開リポジトリ URL |
| `summary_ja` | string | 日本語 1 文要約 |

任意フィールド:

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `license` | string | 確実に分かるライセンス |
| `maturity` | string | `widely-used`, `active`, `established` など |
| `notes` | string | 注意点 |

## 追加例

```json
{
  "id": "example-tool",
  "name": "Example Tool",
  "artifact_type": "tool",
  "domains": ["genomics"],
  "modalities": ["VCF"],
  "tasks": ["annotation"],
  "ecosystems": ["Python"],
  "scales": ["molecular"],
  "official_url": "https://example.org/",
  "repo_url": "https://github.com/example/example-tool",
  "license": "MIT",
  "maturity": "active",
  "summary_ja": "VCF に注釈を付与するための例示ツールです。"
}
```

## 検証

```bash
make validate
make test
```
