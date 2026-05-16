# 初期ランドスケープ

## molecular

ゲノミクス、RNA-seq、single-cell、プロテオミクス、メタボロミクス、マイクロバイオームは、ファイル形式とワークフローの依存が強い領域です。そのため、ライブラリ単体だけでなく、SAMtools/BCFtools、GATK、QIIME 2、nf-core など、公開リポジトリで確認できるパイプラインやツールも同じカタログに含めています。

## cellular and tissue

single-cell、spatial omics、cytometry、細胞画像、病理画像は、分子特徴と細胞/組織構造を接続する中間尺度です。Scanpy、Seurat、SpatialData、Cellpose、StarDist、FlowKit、pycytominer などを同じ尺度タグで横断検索できるようにしています。

## organ-system

EEG/MEG/iEEG は MNE-Python、EEGLAB、FieldTrip、Brainstorm のように言語や GUI の違いが大きく、BIDS や NWB のような標準も解析再現性に直結します。医用画像では DICOM/NIfTI の I/O、registration、segmentation、deep learning が主要な軸になります。

## whole-person and clinical

臨床データは EHR そのもの、FHIR/OMOP の標準、phenotyping、clinical NLP、survival analysis が分かれます。生データを扱う前に、同意、匿名化、アクセス権、監査証跡を明確にする必要があります。

## behavior and psychometrics

行動実験・心理統計では、PsychoPy や jsPsych のようなデータ取得基盤と、lavaan、psych、mirt、lme4、brms のような統計モデリング基盤を分けて整理します。

## population and environmental

コホート、疫学、公衆衛生、地理空間、曝露、移動データはマクロ側の尺度です。EpiNow2、EpiEstim、GeoPandas、PySAL、rexposome、scikit-mobility などを入れ、個人単位データと集団・環境文脈の橋渡しを意識しています。

## privacy and governance

匿名化、差分プライバシー、federated analysis は、解析後処理ではなく設計段階から関与する領域です。OpenDP、diffprivlib、Presidio、ARX、sdcMicro、DataSHIELD などを初期カタログに入れています。
