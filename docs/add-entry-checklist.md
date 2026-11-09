# 項目追加チェックリスト

1. 公式 URL と公開リポジトリ URL を確認します。
2. 同じ ID や同じプロジェクトが既にないか検索します。
3. `artifact_type`, `domains`, `modalities`, `tasks`, `ecosystems`, `scales` を既存タグに寄せます。
4. ライセンス本文または公式パッケージ宣言を読み、利用対象・非商用制限・同梱物の別条件を確認します。GitHub 自動判定や登録簿のライセンスだけで採用しません。
   - 確認日、README・LICENSE URL、ファイルの blob SHA、採録・保留理由を `docs/reviews/` に記録します。
   - repo の移転、archived、同一 repo の別ラッパー、非推奨状態を確認します。
5. `summary_ja` は用途が分かる 1 文にします。
6. `make catalog-page` で全件ページと分野索引を再生成し、`make validate` を実行します。
7. `make test` を実行します。

検索例:

```bash
PYTHONPATH=src python3 -m human_data_lib.cli search FHIR
PYTHONPATH=src python3 -m human_data_lib.cli list --domain microbiome
PYTHONPATH=src python3 -m human_data_lib.cli stats --facet tasks
PYTHONPATH=src python3 -m human_data_lib.cli stats --facet scales
PYTHONPATH=src python3 -m human_data_lib.cli list --scale population
```
