# 継続更新ランドスケープ

## molecular

ゲノミクス、RNA-seq、single-cell、プロテオミクス、メタボロミクス、マイクロバイオームは、ファイル形式とワークフローの依存が強い領域です。そのため、ライブラリ単体だけでなく、SAMtools/BCFtools、GATK、QIIME 2、nf-core など、公開リポジトリで確認できるパイプラインやツールも同じカタログに含めています。

2026-05-18 の更新では、GenomicRanges、SummarizedExperiment、SingleCellExperiment、VariantAnnotation などの Bioconductor 基盤、ProteoWizard、GA4GH VRS/Beacon/WES を追加し、R/Bioconductor と標準 API 側の抜けを補いました。

2026-05-19 の更新では、minfi、methylKit、bsseq、SeSAMe を追加し、DNA methylation array と bisulfite sequencing の公式 Bioconductor 実装を補いました。加えて VSEARCH、CellBender、slingshot、tradeSeq、cell2location を追加し、microbiome、single-cell QC、trajectory、spatial deconvolution の抜けを小さくしました。

2026-05-20 の更新では、HTS Specifications、VCFtools、GLnexus、GLIMPSE2、nf-core/rnaseq、sarek、scrnaseq、methylseq、atacseq、differentialabundance、ampliseq、mag、nf-core/modules、Bioconda recipes、BioContainers を追加し、形式仕様、variant 集団解析、個別 workflow、packaging/container ecosystem までを同じ molecular / infrastructure 軸で検索できるようにしました。

2026-05-21 の更新では、DEXSeq、Arriba、Clair3、Sniffles2、MEGAHIT、ANGSD、GTDB-Tk、Percolator、seqr を追加し、RNA-seq exon usage / fusion、long-read small/SV calling、metagenome assembly / MAG taxonomy、proteomics FDR、rare disease variant review の公式公開 repo を補いました。

2026-05-22 の更新では、clusterProfiler、fgsea、STAR-Fusion、nf-core/rnafusion、AIRR Community Data Standards、Change-O、scRepertoire、immunarch、immuneML、FragPipe を追加し、omics gene set enrichment、RNA-seq fusion workflow、adaptive immune receptor repertoire の標準・解析・machine learning、mass spectrometry proteomics platform を molecular / cellular / infrastructure で検索できるようにしました。MiXCR は公開 repo は確認できましたが、実行ライセンス条件が非営利/商用利用に分かれるため採録しませんでした。

2026-05-27 の更新では、vg、PGGB、Somalier、peddy、Octopus、VarDictJava、IGV、JBrowse 2、SRA Toolkit、SeqKit、seqtk、OpenCGA、CellBase、Comet を追加し、pangenome graph、sample QC、genome browser、public read archive access、sequence utility、clinical genomics data platform、proteomics search engine まで molecular / population / infrastructure の抜けを補いました。Manta、Strelka2、ExpansionHunter は公開 repo は確認できましたが、PolyForm Strict 系の利用条件のため採録しませんでした。

2026-05-31 の更新では、nf-core/chipseq、cutandrun、smrnaseq、raredisease、hlatyping を追加し、epigenomics、small RNA、希少疾患ゲノム、HLA typing の公式 workflow を補いました。加えて TRTools、bioframe、PyRanges、LIMIX を追加し、tandem repeat、genomic interval、genetic mixed model / QTL 解析を molecular / population / infrastructure の横断軸で検索できるようにしました。nf-core/quantms と nf-core/proteomicslfq は archived 状態のため、この run では採録しませんでした。

2026-06-01 の更新では、nf-core/airrflow、taxprofiler、viralrecon、hic、nanoseq、fetchngs、bamtofastq、eager、rnavar、clipseq、circrna を追加し、AIRR-seq、metagenomics、viral genomic epidemiology、3D genomics、long-read、public archive ingestion、RNA variant / CLIP / circRNA workflow を補いました。さらに Rsubread、GffRead、Exomiser、scGLUE、metaMS、CAMERA、LDSC、PRSice-2、bigsnpr、GWASLab、ieugwasr、plinkQC、selscan、ThermoRawFileParser を追加し、read mapping / quantification、transcript annotation、variant prioritization、single-cell multi-omics integration、metabolomics preprocessing、GWAS summary statistics、polygenic score、SNP array QC、selection scan、proteomics raw conversion の抜けを小さくしました。

2026-06-01 の追補更新では、hap.py、Truvari、pbsv、cuteSV、SVIM、GATK-SV、nf-core/oncoanalyser、nf-core/pangenome、MethylDackel、maftools、MutationalPatterns、PureCN、FACETS を追加し、small variant benchmarking、long-read / short-read structural variant、pangenome graph、bisulfite methylation extraction、がん MAF / mutational signature / copy-number 解析の抜けを補いました。さらに mixOmics、TreeSummarizedExperiment、glmGamPoi を追加し、multi-omics 統合、tree-aware assay container、single-cell / RNA-seq count model の横断軸も補いました。

2026-06-02 の更新では、BUSCO、MMseqs2、DIAMOND、SPAdes、Flye、CheckM2、Bakta、anvi'o、Panaroo、FastANI を追加し、metagenomics / microbial genomics の assembly、annotation、taxonomy、MAG 品質評価を補いました。さらに QTLtools、GEMMA、susieR、SUPPA、LeafCutter、MetaMorpheus、ISA-API、EDAM Ontology を追加し、QTL / fine mapping、alternative splicing、proteomics search、study metadata / ontology の抜けを molecular / population / infrastructure から検索できるようにしました。

2026-06-03 の更新では、nf-core/abotyper、alleleexpression、cageseq、circdna、crisprseq、deepmutscan、diaproteomics、drop、metaboigniter、methylarray、methylong、mhcquant、mspepid、pacsomatic、pacvar、phaseimpute、rarevariantburden、riboseq、rnadnavar、rnasplice、tumourevo、variantbenchmarking、variantcatalogue、variantprioritization、viralintegration などを追加し、blood group antigen、allele-specific expression、CAGE、CRISPR、proteomics、metabolomics、rare disease、cancer genomics、variant evaluation / prioritization の workflow coverage を補いました。PyDESeq2、genomic-features、OHDSI Koios も追加し、Python 側の bulk RNA-seq differential expression、genomic feature access、OMOP Genomic vocabulary mapping を molecular / clinical / infrastructure から検索できるようにしました。

2026-06-04 の更新では、nf-core/callingcards、createpanelrefs、createtaxdb、dartseq、demultiplex、denovotranscript、detaxizer、epitopeprediction、fastqrepair、fastquorum、metapep、metatdenovo、nanostring、proteogenomicsdb、readsimulator、references、ribomsqc、seqsubmit を追加し、regulatory genomics、panel of normals / reference model、metagenomic database、m6A、sequencing demultiplex、transcriptome assembly、host-read privacy reduction、epitope、FASTQ repair、UMI consensus、metagenome-to-epitope、Nanostring expression、proteogenomics database、read simulation、reference build、ribonucleoside MS QC、ENA submission の workflow coverage を補いました。GA4GH Data Connect / DRS / WES / Beacon starter kit と compliance、Cat-VRS も追加し、genomic data discovery、workflow execution、variant concept standard の infrastructure 側の抜けを小さくしました。

2026-06-06 の更新では、GEOquery、TCGAbiolinks、AnnotationDbi、ensembldb、ExperimentHub、ChAMP、missMethyl、DMRcate、dmrseq、wateRmelon、CNVRanger、Gviz、DEGreport、apeglm、IHW、RUVSeq を追加し、GEO / TCGA data access、Bioconductor annotation database、DNA methylation array / bisulfite sequencing、CNV、RNA-seq 統計・可視化の抜けを補いました。

## cellular and tissue

single-cell、spatial omics、cytometry、細胞画像、病理画像は、分子特徴と細胞/組織構造を接続する中間尺度です。Scanpy、Seurat、SpatialData、Cellpose、StarDist、FlowKit、pycytominer などを同じ尺度タグで横断検索できるようにしています。

SpatialExperiment、cytomapper、Bio-Formats、OpenSlide、HistomicsTK、Digital Slide Archive、Vitessce、TileDB-SOMA、CELLxGENE Census などを加え、single-cell/spatial data model と病理画像インフラの両側から検索できるようにしています。

TIAToolbox も追加し、whole-slide pathology 画像の読み込み、前処理、特徴抽出、モデル適用を扱う Python toolkit まで tissue / clinical scale で拾えるようにしています。

2026-05-20 の更新では、CELLxGENE explorer、Azimuth、miloR、Harmony、MCMICRO、ASHLAR、starfish、PathML、Slideflow、UCSC Cell Browser、OMERO、OME-NGFF を追加し、single-cell browser、reference mapping、差次的 abundance、multiplex tissue imaging、image-based transcriptomics、WSI deep learning、bioimaging storage / format standard の抜けを補いました。

2026-05-21 の更新では、MOFA2、NicheNet/nichenetr、Baysor、large_image を追加し、multi-omics factor analysis、cell-cell communication、分子座標型 spatial transcriptomics segmentation、whole-slide image tiling / delivery を tissue / cellular / infrastructure で検索できるようにしました。

2026-05-22 の更新では、scRepertoire、Change-O、immunarch、immuneML、AIRR Community Data Standards を追加し、single-cell TCR/BCR や bulk AIRR-seq を細胞・分子の中間尺度として扱う免疫レパトア解析の抜けを補いました。

2026-05-27 の更新では、RAPIDS-SingleCell、scArches、Pegasus、LIANA+、Sopa、VALIS、HistoQC、TissUUmaps、bioformats2raw、raw2ometiff、micro-sam を追加し、GPU single-cell、reference mapping、cell-cell communication、spatial omics workflow、whole-slide registration/QC、OME-Zarr conversion、foundation-model based microscopy segmentation を cellular / tissue / infrastructure で検索できるようにしました。SCENIC+ は non-commercial/proprietary 条件のため採録しませんでした。

2026-05-31 の更新では、nf-core/spatialvi を追加し、Visium などの spatial transcriptomics と tissue image の preprocessing、QC、visualization、reporting を nf-core workflow として tissue / cellular / molecular / infrastructure から検索できるようにしました。

2026-06-01 の更新では、scIB、scib-metrics、scCODA、SpaGCN、mistyR、Voyager を追加し、single-cell integration benchmark、細胞組成解析、spatial domain detection、spatial statistics の横断軸を補いました。加えて cydar、flowAI、CytoView、histolab、wsidicom、cuCIM、btrack、TrackMate、Fiji を追加し、mass cytometry differential abundance、flow cytometry QC / visualization、whole-slide pathology、DICOM WSI、GPU bioimage processing、cell tracking、ImageJ/Fiji ecosystem を tissue / cellular / infrastructure で検索できるようにしました。BANKSY は公開 repo を確認しましたが、commercial usage の制限があるため採録しませんでした。

2026-06-01 の追補更新では、nf-core/imcyto、BPCells、sctransform、zellkonverter、iSEE、dreamlet、muscat、dittoSeq、nnSVG、SpatialFeatureExperiment、imcRtools、PeacoQC、steinbock、scimap、ark-analysis、InstanSeg、DeepProfiler、BioIO、nd2、spatialdata-io、napari-spatialdata を追加し、imaging mass cytometry workflow、大規模 single-cell matrix、AnnData / SingleCellExperiment 変換、cohort-scale single-cell 統計、spatially variable gene、geometry-aware spatial data model、multiplexed tissue imaging、microscopy segmentation / profiling / file I/O を tissue / cellular / infrastructure から検索できるようにしました。

2026-06-02 の更新では、Palantir、MAGIC、MELD、dynamo、SAMap、SeuratDisk、MAESTRO、COMMOT、CellCharter、STalign、spatialLIBD、SPOTlight、Spateo、semla、STUtility を追加し、single-cell trajectory、denoising、RNA velocity、cross-species mapping、Seurat / AnnData 変換、single-cell / spatial workflow、spatial cell-cell communication、spatial registration / deconvolution / 3D modeling を補いました。加えて ASAP、Cytomine、premessa、cytolib、Omnipose、MoBIE Fiji Viewer を追加し、digital pathology annotation、bioimage collaboration、cytometry backend、cell segmentation、大規模 bioimage viewer の coverage を広げました。

2026-06-03 の更新では、nf-core/cellpainting、hadge、hicar、lsmquant、molkart、panoramaseq、pixelator、scdownstream、scnanoseq、spatialaxe、tfactivity、scverse pertpy、pytometry、spatialdata-plot を追加し、高コンテンツ Cell Painting、single-cell donor demultiplexing、HiCAR、light-sheet microscopy、Molecular Cartography、in-situ array spatial transcriptomics、Proximity Network Assay、single-cell downstream QC / integration、single-cell Nanopore、Xenium / Artera、perturbation analysis、cytometry、SpatialData plotting の抜けを cellular / tissue / infrastructure で補いました。

2026-06-04 の更新では、nf-core/marsseq と nf-core/mcmicro、scverse の anndataR / scverse-io / annbatch / Muon.jl / deres、BioImage.IO model zoo / specification / core / napari integration / JDLL を追加し、MARS-seq、multiplex whole-slide imaging、AnnData / MuData interoperability、on-disk AnnData minibatch、single-cell result table、bioimage deep-learning model sharing / validation / inference の抜けを cellular / tissue / infrastructure で補いました。

2026-06-06 の更新では、destiny と celda を追加し、single-cell diffusion map / pseudotime と Bayesian clustering / decontamination の R / Bioconductor 実装を cellular / molecular で検索できるようにしました。ExperimentHub も cellular resource access の infrastructure として扱えるようにしました。

## organ-system

EEG/MEG/iEEG は MNE-Python、EEGLAB、FieldTrip、Brainstorm のように言語や GUI の違いが大きく、BIDS や NWB のような標準も解析再現性に直結します。医用画像では DICOM/NIfTI の I/O、registration、segmentation、deep learning が主要な軸になります。

Brainstorm、SPM、C-PAC、MNE-Connectivity、autoreject、PyPREP、MNE-ICALabel、MNE-NIRS、MNE-BIDS-Pipeline、BrainFlow、Luna、Wonambi、Clinica、BIDScoin、Orthanc、DCMTK、dcm4che、ITK-SNAP、MITK、Lead-DBS などを追加し、EEG/MEG/fNIRS、睡眠、DICOM/PACS、医用画像 annotation まで広げています。

Neo、odML、Braindecode、Plastimatch、Connectome Workbench を追加し、神経電気生理の I/O/metadata、脳信号 deep learning、volumetric registration、HCP 系 connectome 可視化まで確認対象に含めています。

2026-05-20 の更新では、SNIRF、NeuroDOT_py、NeuroConv、MOABB、pyRiemann、tedana、Dcm2Bids、deid、MNE-LSL、MNE-CPP、Pycrostates、PhysioNet Cardiovascular Signal Toolbox、pyVHR、elastix、MONAI Label、Kaapana、TorchXRayVision、OpenBCI GUI を追加し、fNIRS 標準、NWB 変換、BCI benchmark、Riemannian EEG、multi-echo fMRI、BIDS 変換、DICOM de-identification、医用画像 annotation / platform、remote PPG まで広げています。

2026-05-21 の更新では、pybv、MNE-HFO、osl-dynamics、NiMARE、TemplateFlow Client、SDCFlows、ASLPrep、QSIRecon、BIOBSS、SimNIBS を追加し、BrainVision/BIDS I/O、iEEG HFO、M/EEG dynamics、neuroimaging meta-analysis、template access、EPI distortion correction、ASL/dMRI workflow、biosignal pipeline、TMS/tES field modeling を補いました。

2026-05-22 の更新では、HCP Pipelines、ExploreASL、BrainSpace、Boutiques を追加し、Human Connectome Project 型 MRI preprocessing、arterial spin labeling perfusion MRI、connectome gradient analysis、neuroimaging command-line tool descriptor / execution の公式公開 repo を補いました。

2026-05-27 の更新では、OpenNeuro、NiWorkflows、EEGDash、Eelbrain、Frites、OpenMEEG、MNE-Features、naplib-python、mTRF-Toolbox、bids-matlab、CuBIDS、Snakebids、fslpy、FastSurfer、phys2bids、Neurodocker、Neurodesk、Cornerstone3D、Weasis、Wearipedia、wristpy、biosignalsnotebooks、pygt3x、agcounts を追加し、BIDS data sharing/curation、M/EEG statistics、source modeling、auditory neuroscience、MRI workflow/container、web DICOM rendering、wearable/actigraphy data processing の抜けを補いました。

2026-05-31 の更新では、dcmjs と fo-dicom を追加し、JavaScript と .NET / C# の両側から DICOM、DICOM-SR、DICOMweb、PACS networking / storage を扱う実装を organ-system / clinical / infrastructure で確認できるようにしました。

2026-06-01 の更新では、edfio、BioSig、BioPsyKit、BrainStat、MICAPIPE、NiTransforms、Nitime、PlatiPy、PyDicer、dicompyler-core、PhysioZoo、read.gt3x を追加し、EDF/BDF 形式の睡眠・脳波・生理信号 I/O、neuroimaging statistics / connectomics、neuroimaging transform、time-series neurophysiology、radiotherapy DICOM、heart-rate variability、actigraphy raw file 解析を organ-system / whole-person / clinical 側から拾えるようにしました。stepcount は公開 repo を確認しましたが academic-only license のため採録しませんでした。

2026-06-02 の更新では、Homer3、ERPLAB、Unfold Toolbox、OSL-ephys、bycycle、rapidtide、NiBabies、NiFreeze、SigPy、ISMRMRD、ASTRA Toolbox、TIGRE、TomoPy、Core Imaging Library、Forest、gaitmap、mobgap、NimbalWear を追加し、fNIRS、ERP、M/EEG workflow、neural oscillation、fMRI lag / physiology、infant MRI、diffusion MRI、MRI raw data / reconstruction、CT / tomography reconstruction、digital phenotyping、wearable gait / mobility / actigraphy を organ-system / whole-person / clinical / infrastructure で検索できるようにしました。

2026-06-03 の更新では、dMRIPrep、EEGPrep、MEGPrep、MolPrep、PETPrep、PETQC、fMRIPost-rapidtide、fMRIPost-tedana、nondefaced-detector、niquery を追加し、dMRI、EEG、MEG、PET / SPECT、multi-echo fMRI、fMRI physiology postprocessing、画像公開前 privacy check、open neuroimaging dataset query を organ-system / clinical / infrastructure で検索できるようにしました。

2026-06-04 の更新では、pydicom organization の dicom-validator、MONAI Deploy App SDK / Informatics Gateway、OpenNeuro miniqc、OHIF static-wado-js を追加し、DICOM validation、medical imaging AI deployment、DICOM workflow routing、BIDS dataset QC、static DICOMweb conversion を organ-system / clinical / infrastructure 側から検索できるようにしました。

2026-06-06 の更新では、ANTsPy、RNifti、oro.nifti、tractor、Pydra を追加し、Python ANTs registration、R / C++ NIfTI I/O、MRI / tractography data manipulation、Nipype 2.0 系 dataflow engine を organ-system / clinical / infrastructure で検索できるようにしました。neuromaps は公開 repo を確認しましたが non-commercial 条件の license file であったため採録しませんでした。

## whole-person and clinical

臨床データは EHR そのもの、FHIR/OMOP の標準、phenotyping、clinical NLP、survival analysis が分かれます。生データを扱う前に、同意、匿名化、アクセス権、監査証跡を明確にする必要があります。

HL7 FHIR specification、Firely .NET SDK、Google FHIR、OHDSI WebAPI/Ares/Strategus/CDMConnector、OpenSAFELY CLI、i2b2 Core Server、cBioPortal を追加し、標準仕様、SDK、OMOP 運用、secure analytics、がんゲノム臨床ポータルを分けて見られるようにしています。

Inferno Framework と Archie も追加し、FHIR conformance testing と openEHR archetype/reference model 実装を clinical infrastructure 側から確認できるようにしました。

2026-05-20 の更新では、Medplum、LinuxForHealth FHIR Server、Blaze、OpenHIM Core、Open Concept Lab、OHDSI Broadsea、SMART App Launch、FHIRPath、CDS Hooks、Clinical Quality Language、DHIS2 Core、GNU Health HIS、Bahmni、openIMIS を追加し、FHIR server、HIE mediator、terminology service、OMOP deployment、HL7 app/CDS/quality 標準、public-health / hospital information platform を補いました。

2026-05-21 の更新では、ResearchKit、Open mHealth Schemas、Human Phenotype Ontology、Data Use Ontology、OHDSI CohortGenerator、OpenCRVS Core、NextGen Connect、CommCare HQ、OpenSRP FHIR Core、SENAITE Core、HL7 FHIR IG Publisher、HL7 CDA Core 2.0、OpenFn Lightning を追加し、mobile health / consent、wearable schema、phenotype / consent ontology、OMOP cohort generation、civil registration、HL7/FHIR integration、field health platform、LIMS、FHIR IG publishing、clinical document standard、global health workflow automation まで広げています。

2026-05-22 の更新では、FHIR Server for Azure を追加し、HAPI FHIR、Google FHIR、LinuxForHealth FHIR Server、Blaze、Medplum に加えて Microsoft の公開 FHIR server 実装も clinical / infrastructure で検索できるようにしました。

2026-05-27 の更新では、RADAR-base、Beiwe Research Platform、REDCapR、SORMAS、Go.Data、CohortDiagnostics、PheValuator、PheWAS、IncidencePrevalence、PatientProfiles、CodelistGenerator、Android FHIR SDK、Kotlin FHIR、Microsoft FHIR Converter、openEHR REST API Specifications、OBiBa Opal、OBiBa Mica、MOLGENIS EMX2、OpenSpecimen、Open Hospital、HospitalRun、Open Pedigree、CheXpert Labeler、MicrobeTrace を追加し、digital phenotyping、FHIR mobile SDK/conversion、OMOP phenotype diagnostics、cohort/biobank metadata platform、public-health outbreak platform、hospital information system、clinical NLP の clinical / population / infrastructure coverage を広げました。

2026-05-31 の更新では、MatchIt、WeightIt、cobalt、mice、tmle3 を追加し、観察研究の matching / weighting、共変量バランス診断、欠測補完、targeted learning を clinical / population / whole-person で検索できるようにしました。さらに FLamby を追加し、臨床・医用画像データを想定した federated learning benchmark を privacy / clinical infrastructure 側から参照できるようにしました。

2026-06-01 の更新では、OHDSI EvidenceSynthesis、SelfControlledCaseSeries、CaseCrossover、EmpiricalCalibration、Cyclops、ROhdsiWebApi、Andromeda、CirceR、CohortConstructor、MethodEvaluation を追加し、OMOP CDM 上の evidence synthesis、self-controlled design、case-crossover design、empirical calibration、大規模回帰、WebAPI client、disk-backed storage、cohort expression、手法評価を補いました。さらに MedTagger、NegBio、HL7 FHIR Core Java、SMART App Launch JavaScript Client、SMART on FHIR Python Client、OMOP on FHIR、LabKey Server を追加し、clinical NLP、FHIR validation / reference implementation、SMART client、OMOP-FHIR bridge、clinical research data platform の抜けを小さくしました。

2026-06-02 の更新では、fhir-py、fhirpath-py、OHDSI Eunomia、OhdsiRTools を追加し、Python FHIR client / FHIRPath evaluation、OMOP sample dataset 管理、OHDSI R package utility を clinical / infrastructure 側から補いました。

2026-06-03 の更新では、OHDSI CaseControl、CohortIncidence、CohortPathways、CohortPrevalence、CohortExplorer、ConceptSetDiagnostics、Criteria2Query、FhirToCdm、InspectOMOP、DrugAdherence、Aegis、Nostos を追加し、OMOP CDM 上の case-control、incidence、pathway、prevalence、cohort profile visualization、concept set diagnostics、free-text criteria parsing、FHIR-to-OMOP conversion、Python EHR extraction、drug adherence、geospatial epidemiology、text-to-SQL exploration を clinical / population / infrastructure から検索できるようにしました。

2026-06-04 の更新では、DARWIN-EU / OHDSI の DrugExposureDiagnostics、CdmOnboarding、CohortSurvival、TestGenerator、omopgenerics、DrugUtilisation、visOmopResults、CohortCharacteristics、SelfControlledCohort、StandardizedAnalysisAPI、CdmDdlBase、CohortCharacterization を追加し、OMOP drug exposure diagnostics、CDM onboarding、survival analysis、study testing、R object generics、drug utilisation、study result visualization、cohort characterization、self-controlled cohort、standardized analysis exchange、CDM DDL generation を clinical / population / infrastructure で検索できるようにしました。openEHR Reference Models と Java Model Stack も追加し、FHIR / OMOP に加えて openEHR data model の公式 repo coverage を補いました。

2026-06-06 の更新では、fhircrackr、epiR、epitools、Epi を追加し、FHIR XML bundle の R data.frame 化、疫学指標・association measure、cohort / registry follow-up の Lexis / rate / survival analysis を clinical / population 側から補いました。

## behavior and psychometrics

行動実験・心理統計では、PsychoPy や jsPsych のようなデータ取得基盤と、lavaan、psych、mirt、lme4、brms のような統計モデリング基盤を分けて整理します。

Expyriment、JATOS、PsychoJS、Psychtoolbox-3、lavaan、OpenMx、mirt、Systole を追加し、実験実行、オンライン研究、心理物理 timing、尺度・潜在変数解析、心理生理信号を同じ behavioral scale で扱えるようにしています。

2026-05-20 の更新では、KoboToolbox と ActivitySim を追加し、フィールド調査・質問紙収集と activity-based travel modeling を behavioral / whole-person / population の接続点として扱えるようにしました。

2026-05-21 の更新では、easystats、afex、psiTurk、PennController、ODK Collect、Enketo Web Forms を追加し、心理・臨床統計モデルの報告、factorial experiment 解析、オンライン行動実験、心理言語実験、フィールド調査の mobile/web collection を補いました。

2026-05-22 の更新では、TAM を追加し、質問紙・テスト項目データに対する Rasch、2PL、多次元 IRT などの psychometric model 推定を whole-person / behavioral / population で拾えるようにしました。

2026-05-27 の更新では、JASP、jamovi、psych、mousetrap、survey、Pupil、pymovements、PyGaze、Py-Feat、DeepLabCut、pyxform、pyODK、CSPro を追加し、GUI 統計解析、心理測定、complex survey analysis、mouse/eye/facial/pose behavior、ODK/XLSForm/field survey collection まで whole-person / behavioral / population で検索できるようにしました。

2026-06-01 の更新では、BORIS、Experiment Factory、LAMP-cortex、AWARE Framework、SensingKit、SurveyJS、mirtCAT、blavaan、EGAnet、qgraph、metafor、eyetrackingR を追加し、動画・観察セッションの行動 coding、行動実験 battery の container 化 / reproducible deployment、mobile sensing、質問紙・survey UI、computerized adaptive testing、Bayesian latent-variable model、network psychometrics、meta-analysis、eye-tracking 解析を behavioral / whole-person / infrastructure で検索できるようにしました。

2026-06-02 の更新では、semTools と psychonetrics を追加し、lavaan 周辺の SEM 補助、測定不変性、psychological network model、confirmatory network analysis を whole-person / behavioral / population で検索できるようにしました。

2026-06-06 の更新では、catR、lordif、ltm、mokken、sirt、eRm、WrightMap、difR を追加し、computerized adaptive testing、IRT、DIF、Mokken scale analysis、Rasch modeling、item-person map などの心理測定パッケージを whole-person / behavioral / population で検索できるようにしました。

## population and environmental

コホート、疫学、公衆衛生、地理空間、曝露、移動データはマクロ側の尺度です。EpiNow2、EpiEstim、GeoPandas、PySAL、rexposome、scikit-mobility などを入れ、個人単位データと集団・環境文脈の橋渡しを意識しています。

GENESIS、SNPRelate、ADMIXTOOLS 2、epicontacts、incidence2、sf、terra、stars、openair、nasapower を追加し、集団遺伝、公衆衛生 transmission data、R の地理空間・大気環境データ処理を補っています。

simulist、outbreaker2、trackintel を追加し、アウトブレイク line list simulation、伝播経路推定、人間移動軌跡解析を population / behavioral / environmental scale に接続しました。

2026-05-20 の更新では、tskit、msprime、stdpopsim、sgkit、UrbanSim、UrbanAccess、Pandana、pythermalcomfort、Ladybug Tools、epidemics、ggsurveillance を追加し、tree sequence / population genetics simulation、都市・交通 accessibility、built environment / thermal exposure、感染症 scenario modeling と surveillance visualization を補いました。

2026-05-21 の更新では、r5py と City Energy Analyst を追加し、GTFS/OpenStreetMap に基づく travel time / accessibility と都市・地区スケールの building energy / environmental scenario analysis を補いました。

2026-05-22 の更新では、OpenTripPlanner と MobilityDB を追加し、GTFS/OSM に基づく multimodal routing / accessibility analysis と、GPS trace などの spatiotemporal trajectory database を environmental / behavioral / population の接続点として補いました。

2026-05-27 の更新では、r5r、AequilibraE、MATSim、Eclipse SUMO、R5、TransBigData、mobilkit を追加し、travel time matrix、transport assignment、agent-based mobility simulation、traffic microsimulation、GPS/OD/trajectory preprocessing、urban resilience / disaster-risk mobility analysis の public repo を environmental / behavioral / population の接続点として補いました。

2026-05-31 の更新では、sfnetworks、tidytransit、gtfs2gps を追加し、R の sf / tidygraph、GTFS、GPS-like trajectory 変換を使った交通・移動・空間ネットワーク解析を population / environmental / behavioral の接続点として補いました。

2026-06-01 の更新では、Covasim、SynthPops、epichains、cfr、finalsize、readepi、vaccineff、openrouteservice、OSRM、FedData、cf-xarray、CLIMADA、STAC Specification、PySTAC、odc-stac を追加し、感染症 agent-based simulation、合成人口・接触ネットワーク、transmission chain simulation、case fatality ratio、outbreak final size、field epidemiology data reading、vaccine effectiveness、routing / isochrone、環境曝露 covariate 取得、climate / weather array metadata、climate risk、remote sensing / STAC metadata を population / environmental / infrastructure で検索できるようにしました。

2026-06-01 の追補更新では、ipumsr、tigris、rgee、osmdata、spdep、spatialreg、gstat を追加し、IPUMS microdata、Census TIGER/Line、OpenStreetMap、Google Earth Engine、空間重み・空間回帰・geostatistics を population / environmental / infrastructure 側から扱えるようにしました。

2026-06-02 の更新では、Shapely、pyproj、rioxarray、xESMF、Valhalla、pygris、OpenMalaria、EMOD、Starsim、scoringutils、socialmixr、odin を追加し、geometry / projection / raster / climate regridding、routing / map matching、Census geography、感染症 agent-based / ODE simulation、forecast scoring、social contact matrix を population / environmental / behavioral / infrastructure 側から補いました。

2026-06-03 の更新では、nf-core/funcprofiler、funcscan、viralmetagenome、GDAL、PostGIS、QGIS を追加し、microbiome functional profiling、metagenome functional gene screening、viral metagenome reconstruction、raster / vector format conversion、spatial database query、GIS visualization / overlay を population / environmental / infrastructure で検索できるようにしました。

2026-06-04 の更新では、nf-core/pathogensurveillance と nf-core/tbanalyzer、Epiverse-TRACE の serofoi、sivirep、epiversedashboard を追加し、pathogen population genomics、TB complex sequencing、serological force-of-infection estimation、respiratory infection surveillance reporting、outbreak / public-health dashboard の population / clinical coverage を補いました。

2026-06-06 の更新では、surveillance と epiworldR を追加し、communicable disease surveillance count data の aberration detection / endemic-epidemic modeling と、大規模 population を想定した infectious disease agent-based simulation を population / environmental から検索できるようにしました。

## privacy and governance

匿名化、差分プライバシー、federated analysis は、解析後処理ではなく設計段階から関与する領域です。OpenDP、diffprivlib、Presidio、ARX、sdcMicro、DataSHIELD などを継続更新カタログに入れています。

Synthcity、Substra、Toil、miniwdl を追加し、synthetic data、federated analysis、WDL/CWL 実行基盤の公開実装も同じ infrastructure scale で確認できるようにしています。

2026-05-20 の更新では、vantage6、FeatureCloud、GA4GH DRS/TES/TRS/Phenopackets/Service Registry、cwltool、Sapporo Service、RO-Crate、BioCompute Object、CWLProv、DataLad を追加し、federated analysis、GA4GH API 群、workflow execution / provenance、research object packaging、dataset versioning の基盤を厚くしました。

2026-05-21 の更新では、PipelineDP と FederatedScope を追加し、差分プライバシー付き大規模集計と federated learning benchmark / training framework を infrastructure / clinical / population の横断基盤として補いました。

2026-05-22 の更新では、SecretFlow と Boutiques を追加し、MPC/HE/TEE を含む privacy-preserving computation と、解析 tool descriptor の validation / execution framework を infrastructure scale の公開実装として補いました。

2026-05-27 の更新では、Caper、Janis、FedML、Arvados、DATS JSON schemas、TenSEAL、Concrete ML を追加し、WDL/CWL workflow authoring/execution、federated/distributed learning、biomedical big-data provenance、dataset discovery metadata、homomorphic-encryption based privacy-preserving ML まで infrastructure scale の公開実装を厚くしました。

2026-05-31 の更新では、PyDP と FLamby を追加し、差分プライバシー付き集計と医療データ向け federated learning benchmark を privacy / population / clinical / infrastructure の横断基盤として確認できるようにしました。

2026-06-01 の更新では、FedJAX、Splink、anonlink、synthpop、PrimiHub、REANA、Bioschemas、OpenFHE、Microsoft SEAL、DAGitty、EValue を追加し、federated learning simulation、個人レコード linkage / deduplication、privacy-preserving record linkage、synthetic microdata、secure multiparty computation / private set intersection、reproducible analysis workflow、life-science metadata markup、homomorphic encryption、causal DAG / sensitivity analysis を privacy / clinical / population / infrastructure の横断基盤として補いました。

2026-06-02 の更新では、clkhash、scrubadub、pyCANON、Cylc Flow、LinkML、Frictionless Framework、FAIRDOM-SEEK を追加し、privacy-preserving record linkage、text de-identification、anonymity metrics、workflow scheduling、schema modeling、tabular data package validation、FAIR research data / workflow management を infrastructure scale の公開実装として補いました。

2026-06-03 の更新では、nf-core/seqinspector、stableexpression、nascent、omicsgenetraitassociation、diseasemodulediscovery、drugresponseeval を追加し、sequencing QC workflow、stable reference gene selection、nascent transcription、multi-omics trait association、disease module discovery、drug response model evaluation を infrastructure / molecular / clinical の横断基盤として補いました。

2026-06-04 の更新では、nf-core/detaxizer、GA4GH DRS / WES / Beacon starter kit と compliance suite、BioImage.IO specification、openEHR computable reference model を追加し、host sequence reduction、standard implementation testing、model metadata validation、clinical record model governance の infrastructure coverage を補いました。

2026-06-06 の更新では、DataSynthesizer を追加し、sensitive tabular data に対する differential privacy based synthetic data generation を clinical / population / infrastructure の privacy-preserving data sharing として検索できるようにしました。
