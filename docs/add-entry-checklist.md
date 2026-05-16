# 項目追加チェックリスト

1. 公式 URL と公開リポジトリ URL を確認します。
2. 同じ ID や同じプロジェクトが既にないか検索します。
3. `artifact_type`, `domains`, `modalities`, `tasks`, `ecosystems`, `scales` を既存タグに寄せます。
4. ライセンスが確実な場合だけ `license` を入れます。
5. `summary_ja` は用途が分かる 1 文にします。
6. `make validate` を実行します。
7. `make test` を実行します。

検索例:

```bash
PYTHONPATH=src python3 -m human_data_lib.cli search FHIR
PYTHONPATH=src python3 -m human_data_lib.cli list --domain microbiome
PYTHONPATH=src python3 -m human_data_lib.cli stats --facet tasks
PYTHONPATH=src python3 -m human_data_lib.cli stats --facet scales
PYTHONPATH=src python3 -m human_data_lib.cli list --scale population
```
