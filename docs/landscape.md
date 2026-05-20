# 継続更新ランドスケープ

## molecular

ゲノミクス、RNA-seq、single-cell、プロテオミクス、メタボロミクス、マイクロバイオームは、ファイル形式とワークフローの依存が強い領域です。そのため、ライブラリ単体だけでなく、SAMtools/BCFtools、GATK、QIIME 2、nf-core など、公開リポジトリで確認できるパイプラインやツールも同じカタログに含めています。

2026-05-18 の更新では、GenomicRanges、SummarizedExperiment、SingleCellExperiment、VariantAnnotation などの Bioconductor 基盤、ProteoWizard、GA4GH VRS/Beacon/WES を追加し、R/Bioconductor と標準 API 側の抜けを補いました。

2026-05-19 の更新では、minfi、methylKit、bsseq、SeSAMe を追加し、DNA methylation array と bisulfite sequencing の公式 Bioconductor 実装を補いました。加えて VSEARCH、CellBender、slingshot、tradeSeq、cell2location を追加し、microbiome、single-cell QC、trajectory、spatial deconvolution の抜けを小さくしました。

2026-05-20 の更新では、HTS Specifications、VCFtools、GLnexus、GLIMPSE2、nf-core/rnaseq、sarek、scrnaseq、methylseq、atacseq、differentialabundance、ampliseq、mag、nf-core/modules、Bioconda recipes、BioContainers を追加し、形式仕様、variant 集団解析、個別 workflow、packaging/container ecosystem までを同じ molecular / infrastructure 軸で検索できるようにしました。

## cellular and tissue

single-cell、spatial omics、cytometry、細胞画像、病理画像は、分子特徴と細胞/組織構造を接続する中間尺度です。Scanpy、Seurat、SpatialData、Cellpose、StarDist、FlowKit、pycytominer などを同じ尺度タグで横断検索できるようにしています。

SpatialExperiment、cytomapper、Bio-Formats、OpenSlide、HistomicsTK、Digital Slide Archive、Vitessce、TileDB-SOMA、CELLxGENE Census などを加え、single-cell/spatial data model と病理画像インフラの両側から検索できるようにしています。

TIAToolbox も追加し、whole-slide pathology 画像の読み込み、前処理、特徴抽出、モデル適用を扱う Python toolkit まで tissue / clinical scale で拾えるようにしています。

2026-05-20 の更新では、CELLxGENE explorer、Azimuth、miloR、Harmony、MCMICRO、ASHLAR、starfish、PathML、Slideflow、UCSC Cell Browser、OMERO、OME-NGFF を追加し、single-cell browser、reference mapping、差次的 abundance、multiplex tissue imaging、image-based transcriptomics、WSI deep learning、bioimaging storage / format standard の抜けを補いました。

## organ-system

EEG/MEG/iEEG は MNE-Python、EEGLAB、FieldTrip、Brainstorm のように言語や GUI の違いが大きく、BIDS や NWB のような標準も解析再現性に直結します。医用画像では DICOM/NIfTI の I/O、registration、segmentation、deep learning が主要な軸になります。

Brainstorm、SPM、C-PAC、MNE-Connectivity、autoreject、PyPREP、MNE-ICALabel、MNE-NIRS、MNE-BIDS-Pipeline、BrainFlow、Luna、Wonambi、Clinica、BIDScoin、Orthanc、DCMTK、dcm4che、ITK-SNAP、MITK、Lead-DBS などを追加し、EEG/MEG/fNIRS、睡眠、DICOM/PACS、医用画像 annotation まで広げています。

Neo、odML、Braindecode、Plastimatch、Connectome Workbench を追加し、神経電気生理の I/O/metadata、脳信号 deep learning、volumetric registration、HCP 系 connectome 可視化まで確認対象に含めています。

2026-05-20 の更新では、SNIRF、NeuroDOT_py、NeuroConv、MOABB、pyRiemann、tedana、Dcm2Bids、deid、MNE-LSL、MNE-CPP、Pycrostates、PhysioNet Cardiovascular Signal Toolbox、pyVHR、elastix、MONAI Label、Kaapana、TorchXRayVision、OpenBCI GUI を追加し、fNIRS 標準、NWB 変換、BCI benchmark、Riemannian EEG、multi-echo fMRI、BIDS 変換、DICOM de-identification、医用画像 annotation / platform、remote PPG まで広げています。

## whole-person and clinical

臨床データは EHR そのもの、FHIR/OMOP の標準、phenotyping、clinical NLP、survival analysis が分かれます。生データを扱う前に、同意、匿名化、アクセス権、監査証跡を明確にする必要があります。

HL7 FHIR specification、Firely .NET SDK、Google FHIR、OHDSI WebAPI/Ares/Strategus/CDMConnector、OpenSAFELY CLI、i2b2 Core Server、cBioPortal を追加し、標準仕様、SDK、OMOP 運用、secure analytics、がんゲノム臨床ポータルを分けて見られるようにしています。

Inferno Framework と Archie も追加し、FHIR conformance testing と openEHR archetype/reference model 実装を clinical infrastructure 側から確認できるようにしました。

2026-05-20 の更新では、Medplum、LinuxForHealth FHIR Server、Blaze、OpenHIM Core、Open Concept Lab、OHDSI Broadsea、SMART App Launch、FHIRPath、CDS Hooks、Clinical Quality Language、DHIS2 Core、GNU Health HIS、Bahmni、openIMIS を追加し、FHIR server、HIE mediator、terminology service、OMOP deployment、HL7 app/CDS/quality 標準、public-health / hospital information platform を補いました。

## behavior and psychometrics

行動実験・心理統計では、PsychoPy や jsPsych のようなデータ取得基盤と、lavaan、psych、mirt、lme4、brms のような統計モデリング基盤を分けて整理します。

Expyriment、JATOS、PsychoJS、Psychtoolbox-3、lavaan、OpenMx、mirt、Systole を追加し、実験実行、オンライン研究、心理物理 timing、尺度・潜在変数解析、心理生理信号を同じ behavioral scale で扱えるようにしています。

2026-05-20 の更新では、KoboToolbox と ActivitySim を追加し、フィールド調査・質問紙収集と activity-based travel modeling を behavioral / whole-person / population の接続点として扱えるようにしました。

## population and environmental

コホート、疫学、公衆衛生、地理空間、曝露、移動データはマクロ側の尺度です。EpiNow2、EpiEstim、GeoPandas、PySAL、rexposome、scikit-mobility などを入れ、個人単位データと集団・環境文脈の橋渡しを意識しています。

GENESIS、SNPRelate、ADMIXTOOLS 2、epicontacts、incidence2、sf、terra、stars、openair、nasapower を追加し、集団遺伝、公衆衛生 transmission data、R の地理空間・大気環境データ処理を補っています。

simulist、outbreaker2、trackintel を追加し、アウトブレイク line list simulation、伝播経路推定、人間移動軌跡解析を population / behavioral / environmental scale に接続しました。

2026-05-20 の更新では、tskit、msprime、stdpopsim、sgkit、UrbanSim、UrbanAccess、Pandana、pythermalcomfort、Ladybug Tools、epidemics、ggsurveillance を追加し、tree sequence / population genetics simulation、都市・交通 accessibility、built environment / thermal exposure、感染症 scenario modeling と surveillance visualization を補いました。

## privacy and governance

匿名化、差分プライバシー、federated analysis は、解析後処理ではなく設計段階から関与する領域です。OpenDP、diffprivlib、Presidio、ARX、sdcMicro、DataSHIELD などを継続更新カタログに入れています。

Synthcity、Substra、Toil、miniwdl を追加し、synthetic data、federated analysis、WDL/CWL 実行基盤の公開実装も同じ infrastructure scale で確認できるようにしています。

2026-05-20 の更新では、vantage6、FeatureCloud、GA4GH DRS/TES/TRS/Phenopackets/Service Registry、cwltool、Sapporo Service、RO-Crate、BioCompute Object、CWLProv、DataLad を追加し、federated analysis、GA4GH API 群、workflow execution / provenance、research object packaging、dataset versioning の基盤を厚くしました。
