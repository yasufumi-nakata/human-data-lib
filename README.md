# human-data-lib

人間由来バイオデータ解析のためのライブラリ、ツール、標準、ワークフローを横断的に整理するリポジトリです。

公開ページ: <https://www.yasufumi.net/human-data-lib/>

対象は OSS や公式の公開リポジトリで確認できるものに限定します。「人類が作った全部」を厳密に列挙することは公開情報だけでは不可能なので、本リポジトリでは **公開ページで読めるカタログ** と **検索できる Python/CLI 実装** として管理します。

## このページの目的

このページは、人間由来データを扱う解析ソフトウェアを探すための入口です。ゲノムや single-cell のようなミクロなデータから、EHR、医用画像、ウェアラブル、疫学、環境曝露、人口規模データのようなマクロなデータまで、公開リポジトリで確認できる解析資産を同じ形式で並べています。

収録対象は「使える名前の一覧」ではなく、後から検証・検索・比較できる台帳です。各項目には、分野、データ種別、処理タスク、実行環境、解析スケール、公式 URL、公開 repo URL、日本語要約を持たせています。

## まず見る場所

- [全件カタログ](catalog.md): 収録している 595 件をページ上で一覧できます。
- [分類と運用方針](docs/catalog-policy.md): 何を収録し、何を除外するかを確認できます。
- [スキーマ説明](docs/schema.md): 各項目に入っている情報の意味を確認できます。
- [領域別の見取り図](docs/landscape.md): ミクロからマクロまでの対象領域を俯瞰できます。
- [追加時の確認手順](docs/add-entry-checklist.md): 新しい項目を追加するときの確認手順です。

## このサイトで見られるもの

- 全 595 件の公開 OSS / 公開リポジトリ付きカタログ
- 解析スケール別の件数と分類
- 分野、データ種別、処理タスク、実行環境、公式ページ、repo へのリンク
- 日本語の 1 文要約
- 収録方針、除外方針、追加時の確認手順

開発者向けには、同じ内容を元データと Python/CLI からも利用できます。

## 収録状況

2026-05-21 時点の継続更新カタログは 595 件です。代表的な収録軸は以下です。

- ミクロ: ゲノム、変異、RNA-seq、single-cell、spatial omics、プロテオミクス、メタボロミクス、マイクロバイオーム
- 細胞・組織: cytometry、細胞画像、病理画像、空間トランスクリプトミクス
- 臓器・個体: EEG/MEG/iEEG、MRI/fMRI/CT/DICOM、ECG/PPG、睡眠、ウェアラブル、生体信号
- 臨床・集団: EHR、FHIR、OMOP、clinical NLP、コホート、疫学、公衆衛生、集団遺伝
- 行動・環境: 心理統計、行動実験、移動データ、地理空間、環境曝露、建成環境
- 基盤: workflow engine、データ標準、プライバシー保護、federated analysis、差分プライバシー

2026-05-20 の更新では、nf-core 個別 workflow、HTS/GA4GH/HL7/RO-Crate/CWL provenance などの標準、OME/OMERO と pathology/bioimaging、fNIRS/EEG/fMRI/DICOM/physiology、FHIR/OMOP 周辺 platform、population genetics、疫学、公衆衛生、mobility、built environment / thermal exposure の公開 repo を横断的に追加しました。

2026-05-21 の更新では、long-read variant caller、RNA-seq fusion / exon usage、multi-omics factor analysis、spatial segmentation、neuroimaging workflow、mobile health / survey collection、FHIR/HL7 implementation support、clinical/public-health platform、behavioral experiment platform、mobility / built environment、privacy / federated analysis までを再確認し、公式または準公式の公開 repo が確認できる 46 件を追加しました。

## 対象領域

継続更新カタログは、公式の公開リポジトリを確認できる代表的な公開エコシステムを中心に、ミクロからマクロまでの尺度を含みます。

- `molecular`: ゲノム、変異、転写、タンパク質、代謝物、マイクロバイオーム
- `cellular`: single-cell、cytometry、細胞画像、細胞状態
- `tissue`: spatial omics、病理画像、組織画像
- `organ-system`: EEG/MEG、MRI/CT、ECG/PPG、睡眠、生体信号
- `whole-person`: 行動、心理、質問紙、個人単位アウトカム
- `behavioral`: 実験課題、移動、反応時間、行動ログ
- `clinical`: EHR、FHIR、OMOP、医用画像、clinical NLP
- `population`: コホート、疫学、公衆衛生、集団遺伝
- `environmental`: 地理空間、曝露、移動、建成環境
- `infrastructure`: 標準、ワークフロー、データモデル、プライバシー基盤

分野としては次を広く含みます。

- ゲノミクス、変異解析、遺伝統計
- RNA-seq、single-cell、spatial/multi-omics
- プロテオミクス、メタボロミクス、マイクロバイオーム
- EEG/MEG/iEEG、睡眠、生体信号、ウェアラブル
- MRI/fMRI/CT/DICOM、病理画像、bioimaging
- EHR、FHIR、OMOP、clinical NLP
- 行動実験、心理統計、psychometrics
- 匿名化、差分プライバシー、federated analysis
- Nextflow、Snakemake、CWL、WDL、Galaxy などの workflow ecosystem

## 使い方

開発環境から直接実行できます。

```bash
PYTHONPATH=src python3 -m human_data_lib.cli validate
PYTHONPATH=src python3 -m human_data_lib.cli stats --facet domains
PYTHONPATH=src python3 -m human_data_lib.cli stats --facet scales
PYTHONPATH=src python3 -m human_data_lib.cli search single-cell --ecosystem Python
PYTHONPATH=src python3 -m human_data_lib.cli list --scale population
PYTHONPATH=src python3 -m human_data_lib.cli list --scale environmental
PYTHONPATH=src python3 -m human_data_lib.cli list --domain clinical-data --format markdown
PYTHONPATH=src python3 -m human_data_lib.cli show scanpy
```

検索例:

- `--scale molecular`: 分子・オミクス系の解析資産を見る
- `--scale cellular`: single-cell や cytometry を見る
- `--scale clinical`: EHR、FHIR、医用画像、clinical NLP を見る
- `--scale population`: 疫学、公衆衛生、コホート、集団解析を見る
- `--scale environmental`: 曝露、地理空間、移動、建成環境を見る

パッケージとして入れる場合:

```bash
python3 -m pip install -e .
human-data-lib search EEG --domain neurophysiology
```

Python から使う場合:

```python
from human_data_lib import load_catalog

catalog = load_catalog()
entries = catalog.search("single-cell", ecosystem="Python")
for entry in entries:
    print(entry.id, entry.name, entry.official_url)
```

## カタログの考え方

1 件の項目は、ライブラリだけではなく、ツール、標準仕様、ワークフロー、プラットフォーム、エコシステムも含みます。バイオデータ解析では、実務上「ライブラリ」だけを見ても再現性や運用が閉じないためです。

必須項目:

- `id`: 安定した小文字 ID
- `name`: 表示名
- `artifact_type`: `library`, `tool`, `workflow`, `standard`, `platform`, `ecosystem` など
- `domains`: 分野
- `modalities`: データ種別
- `tasks`: 処理段階
- `ecosystems`: 言語、実行環境、周辺エコシステム
- `scales`: `molecular` から `environmental` までの解析尺度
- `official_url`: 公式サイト、公式 docs、公式 GitHub のいずれか
- `repo_url`: 公式または準公式の公開リポジトリ
- `summary_ja`: 日本語 1 文要約

詳しくは [docs/catalog-policy.md](docs/catalog-policy.md) と [docs/schema.md](docs/schema.md) を参照してください。

## 追加方針

新しい項目を追加するときは、公式ページと公開リポジトリを確認し、不確かな最新バージョンや利用者数は書きません。ライセンスも確実に分かる場合だけ記入します。

```bash
make validate
make test
```

上記が通る状態を保ってください。

## スコープ外

- 非公開の企業内・研究室内ライブラリの完全列挙
- 公式の公開リポジトリを確認できない項目
- 公式情報で確認できないバージョン番号、利用者数、性能値の断定
- 個人情報や実データの保存
- 医療判断そのものの自動化

本リポジトリは、解析実装の選定、比較、監査、再現性確保を支援するための土台です。

## 継続更新

公開 OSS は常に増えるため、この一覧は固定版ではありません。平日 11 時に、新しく見落としている公開リポジトリがないかを確認する運用にします。追加候補が見つかった場合は、公式ページと公開 repo URL を確認したうえでカタログ、ドキュメント、検証結果を更新します。
