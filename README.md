# human-data-lib

人間由来バイオデータ解析のためのライブラリ、ツール、標準、ワークフローを横断的に整理するリポジトリです。

公開ページ: <https://www.yasufumi.net/human-data-lib/>

対象は OSS や公式の公開リポジトリで確認できるものに限定します。「人類が作った全部」を厳密に列挙することは公開情報だけでは不可能なので、本リポジトリでは **公開ページで読めるカタログ** と **検索できる Python/CLI 実装** として管理します。

## このページの目的

このページは、人間由来データを扱う解析ソフトウェアを探すための入口です。ゲノムや single-cell のようなミクロなデータから、EHR、医用画像、ウェアラブル、疫学、環境曝露、人口規模データのようなマクロなデータまで、公開リポジトリで確認できる解析資産を同じ形式で並べています。

収録対象は「使える名前の一覧」ではなく、後から検証・検索・比較できる台帳です。各項目には、分野、データ種別、処理タスク、実行環境、解析スケール、公式 URL、公開 repo URL、日本語要約を持たせています。

## まず見る場所

- [検索・絞り込み付きカタログ](https://www.yasufumi.net/human-data-lib/): 日本語カードを読みながら、名前・分野・スケール・実行環境で探せます。
- [全件カタログ](catalog.md): 収録している 1368 件をページ上で一覧できます。
- [分野・解析スケール別索引](docs/catalog-index.md): 分類から各項目へ直接移動できます。
- [2026-11-09 調査・品質点検報告](docs/catalog-review-2026-11-09.md): 新規142件、移転20件、archived 6件、未確認範囲、保留理由と出典を確認できます。
- [分類と運用方針](docs/catalog-policy.md): 何を収録し、何を除外するかを確認できます。
- [スキーマ説明](docs/schema.md): 各項目に入っている情報の意味を確認できます。
- [領域別の見取り図](docs/landscape.md): ミクロからマクロまでの対象領域を俯瞰できます。
- [追加時の確認手順](docs/add-entry-checklist.md): 新しい項目を追加するときの確認手順です。

## このサイトで見られるもの

- 全 1368 件の公開 OSS / 公開リポジトリ付きカタログ
- 解析スケール別の件数と分類
- 分野、データ種別、処理タスク、実行環境、公式ページ、repo へのリンク
- 日本語の 1 文要約
- 収録方針、除外方針、追加時の確認手順

開発者向けには、同じ内容を元データと Python/CLI からも利用できます。

## 検索画面の使い方とロジック

トップページは依存ライブラリを追加しない静的HTML/CSS/JavaScriptです。`index.html` が画面、`assets/site.css` がレスポンシブ表示、`assets/catalog.mjs` が検索・描画を担当します。大量の列を一度に並べる代わりに、日本語要約・主な分類・公式リンクをカードに表示し、詳細欄で全分類、ライセンス、状態、備考を確認できます。

### 検索・絞り込み

1. ブラウザが `src/human_data_lib/data/libraries.json` を読み込みます。収録件数・更新日・分野数・フィルター候補も同じJSONから計算し、画面専用のデータを複製しません。
2. キーワードと各項目の検索文字列をUnicode NFKCで正規化し、英字を小文字にします。全角の `ＥＥＧ` でも `EEG` を検索できます。名前、ID、日本語要約、分類、URL、ライセンス、状態、備考を検索対象にします。
3. キーワードを空白で分割し、**すべての語を含む項目**を残します（AND部分一致）。例: `EEG Python` は両方の語を含む項目です。語が同じフィールドにある必要はありません。入力後180ms待って検索し、「検索する」でも即座に反映します。
4. 解析スケール・分野・実行環境・種類・データ種別・処理タスク・状態の選択は、JSONのタグ値への**完全一致**です。指定した条件同士もANDで組み合わせます。選択肢の括弧内の数は全カタログでの件数で、条件を組み合わせた実際の件数は結果欄に表示します。
5. 初期状態ではアーカイブ済みも含めて表示し、該当項目に状態を明示します。「アーカイブ済みの項目を除外する」を選んだ場合だけ `maturity == "archived"` を除外します。ライセンス・状態の空欄を「確認済み」とは扱いません。
6. 一致した項目を名前順（英字の大小を区別しない比較、同名はID順）または元JSONの収録順に並べ、**24件ずつ**描画します。条件変更時は1ページ目に戻り、範囲外のページ番号は存在する最終ページまで補正します。0件時は条件クリアの導線を表示します。

「EEG / 脳波」「Single-cell」などの検索ヒントは、他の条件をクリアして、そのキーワードだけの検索を開始します。全件表と分野・解析スケール別索引も引き続き利用できます。

### URL・アクセシビリティ・障害時の動作

- 検索語 `q`、分類条件、並び順 `sort`、ページ番号 `page`、アーカイブ除外 `hideArchived` をURLに保持します。再読み込みやブラウザの戻る・進むで条件を復元できます。項目リンクは `?entry=<id>#<id>` でその1件を表示します。
- 入力欄にはラベルを付け、結果件数の変更をライブ領域で通知します。詳細は標準の `details` / `summary`、ページ送り後は結果件数へフォーカスを移します。本文へのスキップリンクとフォーカス表示を用意し、画面幅に応じて1〜3列に切り替えます。
- JSONの文字列は `textContent` で描画し、HTMLとして解釈しません。外部リンクは `http:` / `https:` のURLだけを許可します。
- 取得が15秒で完了しない場合やHTTP/JSONエラー時は、再試行ボタンと全件表へのリンクを表示します。JavaScript無効時も全件表へ移動できます。検索のための外部API、解析トラッキング、外部フォントは使いません。
- 検索処理はブラウザ内ですが、共有・再読み込み時のURLには検索語が含まれます。個人情報・機微な情報は検索欄へ入力しないでください。

Python/CLIも同じJSONを読み、空白区切りのAND部分一致と分類条件の積で検索します。CLIは `casefold()` による大小文字の正規化であり、画面側のNFKC変換やページ分割は行いません。CLIの分類タグ指定は部分一致（種類は完全一致）、画面の選択式フィルターは完全一致です。これらの正規化・分類照合・表示順の違いは意図的です。

## データの検証・生成・公開の仕組み

### 正本と品質確認

正本は [`libraries.json`](src/human_data_lib/data/libraries.json) です。追加時は公式情報・公開リポジトリ・利用条件を確認し、証拠と保留理由を調査報告に残します。`src/human_data_lib/catalog.py` は必須フィールド、空文字、タグ重複、ID形式・重複、HTTP(S) URLのホスト、実在する更新日を検証します。リポジトリURLは末尾の `/` や `.git`、ホスト名の大小文字、GitHubのパスの大小文字を正規化して重複を検知し、同一ソースを共有する既知の別エントリは例外理由を明記します。これは機械的な整合検証であり、全URLへの接続・ライセンスの法的判断・性能保証を自動で行うものではありません。

### 生成フロー

```text
src/human_data_lib/data/libraries.json（正本）
  ├─ ブラウザのfetch → 検索・フィルタ → カード表示（index.html）
  ├─ Python Catalog → CLI検索 / 統計 / 出力
  └─ tools/render_catalog_page.py
       ├─ catalog.md（全件表、安定したIDアンカー）
       └─ docs/catalog-index.md（分野・スケール別索引）

GitHub Pages / Jekyll
  ├─ index.html、assets/*、JSONを静的配信
  └─ Markdown文書 → _layouts/default.html → .html
```

`make catalog-page` は正本から全件表と分類索引を再生成します。索引はタグ別に項目をまとめ、名前順で全件表のIDアンカーへリンクします。複数のタグを持つ項目は複数の索引に現れます。共通レイアウトは検索画面への導線と本文幅を統一し、横長の表にはキーボードでも操作できるスクロール領域を付けます。生成済みの `catalog.md` と `docs/catalog-index.md` を直接手修正せず、正本または生成スクリプトを変更してください。

### 更新手順と検証

Python 3.11以降を使用します。画面の検索ロジックのテストにはNode.js 18以降が必要です（追加npmパッケージは不要です）。

```bash
# 1. 正本と出典・調査記録を更新した後に実行
make catalog-page
make validate
make test
node --test tests/catalog-ui.test.mjs

# 2. 再生成で追加の差分が出ないことを確認
make catalog-page
git diff --exit-code -- catalog.md docs/catalog-index.md

# 3. トップページをローカルで確認
python3 -m http.server 8765
# http://localhost:8765/ を開く（file://ではfetch制約があります）
```

`make test` はカタログ・CLI・監査証拠・生成物一致・HTMLのラベル/ID/ファイル参照を検証し、Node.jsがある環境では画面検索の6テストも実行します。Node.jsがない場合のスキップを「画面テスト成功」とは扱わず、明示した `node --test` も実行してください。JavaScriptテストは全文検索、全角/日本語、AND絞り込み、並び順、項目リンク、アーカイブ除外、URL状態の往復、危険なリンクスキームを確認します。

静的HTTPサーバーはMarkdown/Liquidを変換しません。文書の `.html` 導線はJekyllビルドまたはPages上で確認します。main反映後はGitHub ActionsのCatalog validationとPagesビルド/デプロイが同じcommitで成功したことを確認し、公開ページでも件数、検索、絞り込み、0件、ページ送り、詳細、戻る・進む、文書導線を確認します。ソースのpush成功とPagesの反映成功は別の状態です。

詳細な構成と確認項目は [公開サイトの表示・検証](docs/site-interface.md) を参照してください。

## 収録状況

2026-11-09 時点の継続更新カタログは 1368 件です。代表的な収録軸は以下です。

- ミクロ: ゲノム、変異、RNA-seq、single-cell、spatial omics、プロテオミクス、メタボロミクス、マイクロバイオーム
- 細胞・組織: cytometry、細胞画像、病理画像、空間トランスクリプトミクス
- 臓器・個体: EEG/MEG/iEEG、MRI/fMRI/CT/DICOM、ECG/PPG、睡眠、ウェアラブル、生体信号
- 臨床・集団: EHR、FHIR、OMOP、clinical NLP、コホート、疫学、公衆衛生、集団遺伝
- 行動・環境: 心理統計、行動実験、移動データ、地理空間、環境曝露、建成環境
- 基盤: workflow engine、データ標準、プライバシー保護、federated analysis、差分プライバシー

2026-05-20 の更新では、nf-core 個別 workflow、HTS/GA4GH/HL7/RO-Crate/CWL provenance などの標準、OME/OMERO と pathology/bioimaging、fNIRS/EEG/fMRI/DICOM/physiology、FHIR/OMOP 周辺 platform、population genetics、疫学、公衆衛生、mobility、built environment / thermal exposure の公開 repo を横断的に追加しました。

2026-05-21 の更新では、long-read variant caller、RNA-seq fusion / exon usage、multi-omics factor analysis、spatial segmentation、neuroimaging workflow、mobile health / survey collection、FHIR/HL7 implementation support、clinical/public-health platform、behavioral experiment platform、mobility / built environment、privacy / federated analysis までを再確認し、公式または準公式の公開 repo が確認できる 46 件を追加しました。

2026-05-22 の更新では、gene set enrichment、RNA fusion workflow、AIRR immune repertoire standard / analysis / ML、proteomics suite、HCP/ASL/connectome neuroimaging workflow、FHIR server、psychometrics、mobility / trajectory database、privacy-preserving computation の公開 repo を再確認し、公式または準公式の公開 repo が確認できる 19 件を追加しました。MiXCR は公開 repo は確認できましたが、実行ライセンス条件が非営利/商用利用に分かれるため、この run では採録しませんでした。

2026-05-27 の更新では、pangenome graph、genome QC、genome browser、SRA/sequence utility、OpenCB genomic platform、single-cell/spatial/pathology imaging、OpenNeuro/BIDS/neurophysiology/medical imaging/wearables、FHIR/openEHR/OMOP/DARWIN/OBiBa/public-health/HIS、psychometrics/eye tracking/survey/mobility/workflow/privacy standard 周辺を再確認し、公式または準公式の公開 repo と OSS 条件を確認できる 105 件を追加しました。Manta、Strelka2、ExpansionHunter、pyPPG、SCENIC+、OpenFace、OpenPose などは利用条件が非 OSS または制限付きのため採録しませんでした。

2026-05-31 の更新では、nf-core の ChIP-seq / CUT&RUN / small RNA-seq / rare disease / HLA typing / spatial transcriptomics workflow、tandem repeat と genomic interval、genetic mixed model、因果推論・欠測補完、DICOM JavaScript / .NET、federated learning / differential privacy、交通・地理空間ネットワーク解析の公開 repo を再確認し、公式または準公式の公開 repo を確認できる 22 件を追加しました。nf-core/quantms と nf-core/proteomicslfq は公開 repo は確認できましたが archived 状態のため、この run では採録しませんでした。

2026-06-01 の更新では、nf-core の AIRR / taxonomic profiling / viral recon / Hi-C / Nanopore / CLIP-seq / circRNA などの workflow、Rsubread / GffRead / Exomiser / scGLUE などの omics 実装、single-cell / spatial omics benchmark と spatial statistics、cytometry、digital pathology / microscopy、神経画像・DICOM・放射線治療・生理信号、睡眠・ウェアラブル・行動実験、OHDSI HADES、SMART on FHIR、clinical NLP、心理統計・質問紙・eye tracking、集団遺伝、感染症・合成人口、環境曝露・routing・STAC、workflow / metadata standard、record linkage / privacy-preserving computation の公開 repo を再確認し、公式または準公式の公開 repo と OSS 条件を確認できる 107 件を追加しました。BANKSY、stepcount、SearchGUI / PeptideShaker、OpenClinica は公開 repo は確認できましたが、利用条件または license file の確認条件を満たさないため、この run では採録しませんでした。同日の追補更新では、long-read / structural variant benchmarking、がん MAF / copy-number、single-cell / spatial omics / cytometry / microscopy I/O、nf-core onco/pangenome/imaging-cytometry、IPUMS / Census / OpenStreetMap / Earth Engine、R spatial epidemiology 周辺の公開 repo を再確認し、44 件を追加しました。

2026-06-02 の更新では、metagenomics / microbial genomics、QTL / fine mapping、proteomics、ISA / EDAM metadata、single-cell trajectory / spatial omics / digital pathology / cytometry、EEG/fNIRS/MEG、MRI/CT reconstruction、wearable mobility、FHIR / OMOP utilities、psychometrics、public-health simulation、geospatial exposure、privacy / anonymization、workflow / FAIR data platform 周辺の公開 repo を再確認し、公式または準公式の公開 repo と OSS 条件を確認できる 82 件を追加しました。PHATE、CellOracle、KielMAT、rMATS-turbo、Cytomine-core、RSEM、MetaBAT2 などは、利用条件、archived 状態、既存重複、または license / 公式性の確認不足により採録しませんでした。

2026-06-03 の更新では、nf-core の blood group / allele expression / CAGE / CRISPR / proteomics / metabolomics / rare disease / spatial / variant / viral integration 系 workflow、NiPreps の dMRI / EEG / MEG / PET preprocessing と neuroimaging privacy / query tools、scverse の PyDESeq2 / pertpy / cytometry / genomic feature / SpatialData plotting、OHDSI の case-control / incidence / pathway / prevalence / concept-set / FHIR-to-OMOP / OMOP geospatial / text-to-SQL 周辺、GDAL / PostGIS / QGIS などの geospatial exposure 基盤を再確認し、公式または準公式の公開 repo と OSS 条件を確認できる 86 件を追加しました。nf-core/quantms と nf-core/proteomicslfq は archived 状態のままのため引き続き採録していません。

2026-06-04 の更新では、nf-core の Calling Cards / panel references / taxonomy DB / DART-seq / demultiplex / de novo transcriptome / host-read detaxizing / epitope / FASTQ repair / UMI consensus / MARS-seq / MCMICRO / metapep / metatranscriptome / Nanostring / pathogen surveillance / proteogenomics DB / read simulation / references / ribonucleoside MS QC / ENA submission / TB analysis workflow、DARWIN-EU / OHDSI の OMOP drug exposure diagnostics、CDM onboarding、survival、test generation、generics、drug utilisation、result visualization、cohort characterization、self-controlled cohort、standardized analysis API、CDM DDL、GA4GH Data Connect / DRS / WES / Beacon starter kit と compliance、scverse の AnnData / MuData I/O、BioImage.IO、DICOM / MONAI Deploy / OpenNeuro miniQC、openEHR、Epiverse-TRACE の公開 repo を再確認し、公式または準公式の公開 repo と OSS 条件を確認できる 62 件を追加しました。Epiverse-TRACE linelist / epiparameter は既存収録済み、nf-core/gwas は under construction 表記、OpenClinica は今回もライセンス条件を十分に確認できないため採録しませんでした。

2026-06-06 の更新では、Bioconductor の GEO / TCGA data access、annotation、DNA methylation、single-cell、CNV、RNA-seq 統計、CRAN の疫学・心理測定、FHIR flattening、R / Python neuroimaging I/O、Nipype 系 workflow engine、synthetic tabular data privacy の公開 source を再確認し、公式または準公式の公開 repo と OSS 条件を確認できる 39 件を追加しました。neuromaps は公開 repo は確認できましたが non-commercial 条件の license file であったため採録しませんでした。

2026-06-13 の更新では、Bioconductor の基盤データ構造 / I/O / cache、GA4GH の htsget / refget / Crypt4GH / GKS 実装、BIDS schema / Stats Models / metadata conversion、pydicom の JPEG/DICOM plugin、DARWIN EU / OHDSI の OMOP 結果管理・可視化・phenotyping、nf-core/msproteomics の公開 repo を再確認し、公式または準公式の公開 repo を確認できる 39 件を追加しました。nf-core の未収録 repo には training、設定、under construction、非ヒト中心のものが多いため、今回の採録は human-derived bio-data analysis に直接関係するものへ絞りました。

2026-08-12 の更新では、gget、moscot、MNE denoising / RSA、NiPreps reporting、physiology denoising、nf-core の spatial omics / microbiome workflow、OpenSim / OpenCap の human movement processing を追加し、公式 docs・公開 repo・ライセンスを確認しました。RAPIDS-SingleCell は同一 repo の canonical URL 表記へ修正しました。archived、under construction、discontinued、ライセンス確認不足、テンプレート状態の候補は採録していません。

2026-08-13 の更新では、ehrapy、fibertools-rs、dysgu、pymzML、MicrobiomeStat、HoVer-Net、scFates、SURVIVOR、VitalDB の openvital / vitalutils / openecg、GA4GH Quality Control of WGS / htsget Reference Server を追加しました。EHR、long-read / structural variant、質量分析、microbiome、病理画像、single-cell trajectory、ECG / PPG、生体波形、WGS QC、genomic streaming の公開実装を補っています。pyPPG は公式 repo の academic research only 条件、nf-core/rnastructurome は development version、openeeg は early alpha、opendsp は汎用 DSP、旧 pyvital と mirror は採録条件外のため追加していません。

2026-11-09 の横断調査では、scverse 公式登録簿の全133項目を既存台帳と照合し、臨床試験の pharmaverse、薬物動態、音声・瞳孔・運動計測、プロテオミクス、システム生物学、神経科学メタデータ標準まで探索して142件を追加しました。追加項目は公式 README とライセンス本文または公式パッケージ宣言を確認し、証拠 URL・blob SHA・確認日を記録しています。既存の GitHub repo 1,105件について存在と移転・archived を全件照合し、移転20件と archived 6件を反映しました。公式登録簿や GitHub のライセンス自動判定だけでは OSS と判断せず、非商用条件、利用条件未確認、旧版保守終了などを保留表へ分離しました。詳細と検証範囲は[調査報告](docs/catalog-review-2026-11-09.md)を参照してください。

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
