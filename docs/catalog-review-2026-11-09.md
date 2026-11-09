# 2026-11-09 横断収集・品質点検報告

## 結果

- 1,226件から **1,368件へ、142件追加**しました。追加件数は重複を除いたカタログの利用単位です。
- 既存 GitHub repo を持つ **1,105件を全件API照合**しました。移転20件を現在の公式 repo URL に更新し、archived 6件を利用注意として明示しました。
- scverse 公式登録簿の **133項目すべてを照合**しました。既存・今回追加を合わせ119項目がカタログに対応し、14項目は保留・対象外としました。133はこの調査で取得した登録簿スナップショットの件数であり、サイト表示件数やすべての single-cell ソフトの総数ではありません。
- 新規142件について公式 README とライセンス本文または公式パッケージ宣言を確認し、確認日・URL・blob SHA・採録判断を保存しました。登録簿と実際のライセンスが異なる場合は一次情報を優先しました。
- 分野・解析スケール索引、項目への直接リンク、ライセンス・保守状態・注意点の表示を追加しました。

## 読み方

- [全件カタログ](../catalog.md)
- [分野・解析スケール別索引](catalog-index.md)
- [新規項目の一次出典と保留理由、登録簿全件照合（JSON）](reviews/2026-11-09-source-review.json)
- [既存1,226件のrepo監査結果（JSON）](reviews/2026-11-09-existing-repository-audit.json)

ライセンス欄は原則として当該プロジェクトの本体コードまたは仕様の条件です。依存ライブラリ、学習済みモデル、外部API、入力データ、機器 SDK、配布バイナリに同じ条件が適用されるとは限りません。仕様文書の CC-BY とコードの OSS ライセンスも区別してください。収録は安全性・性能・保守継続・医療用途の承認を保証しません。

## 調査経路と採録方針

1. 作業開始時に main の checkout と `git pull --ff-only` で同期を確認しました。基点は `655cc1c86712eb54188d3f1ca3c54897ebc326dc` です。
2. 既存台帳のID・名称・repo URL・分野・スケールを棚卸ししました。GitHub URL は実体の repository ID、移転先、archived、自動検出ライセンスをAPIで照合しました。
3. 分野横断のWeb検索から公式プロジェクトサイト、公式登録簿、開発者 README、LICENSE、R DESCRIPTION へたどりました。紹介記事や論文は発見用とし、採録内容は公式 source を優先しています。
4. scverse は全登録項目を既存台帳と突き合わせました。pharmaverse、AlphaPept/MannLabs、GA4GH、HED、openMINDS、OpenCOR、COBRA、生体信号・音声・運動・瞳孔計測の公開実装を追加調査しました。
5. 明らかな別名・移転先は重複追加せず既存IDを保持しました。OpenMS / pyOpenMS は同一ソースの C++/CLI 本体と Python API という異なる利用単位のため例外として説明を残しました。
6. 登録簿のライセンス表記とGitHubの自動検出結果が一致しなくても、LICENSE 本文・公式宣言を読み直しました。非商用限定の CellOracle は採録していません。AlphaRaw のように制限付き vendor binary を同梱するものも、単純なOSSとしては追加しませんでした。

主な公式探索入口：
- [scverse packages](https://scverse.org/packages/) / [今回照合した登録簿の固定スナップショット](https://github.com/scverse/ecosystem-packages/tree/6af520ed4a4d8731ef43dbd69838f2ddb9f0a308)
- [pharmaverse](https://pharmaverse.org/) / [臨床データ処理の公式例](https://pharmaverse.github.io/examples/)
- [AlphaPept ecosystem](https://alphapept.org/) / [MannLabs](https://github.com/MannLabs)
- [GA4GH Phenopackets](https://www.ga4gh.org/product/phenopackets/) / [GA4GH VRS Python](https://github.com/ga4gh/vrs-python)
- [HED specification](https://github.com/hed-standard/hed-specification) / [openMINDS](https://github.com/openMetadataInitiative/openMINDS)
- [BioSimulators tools](https://docs.biosimulations.org/users/biosimulators-packages/) / [Pyomeca](https://pyomeca.github.io/) / [Praat source](https://praat.org/download_sources.html)

## 新規142件

詳細な分類は索引に統合しています。以下の出典は調査時に内容を取得した一次情報です。

| 項目 | 用途 | 本体ライセンス | 一次出典 |
| --- | --- | --- | --- |
| [admiral](../catalog.md#admiral) | 臨床試験の SDTM データなどから CDISC ADaM 解析データを構築する R パッケージです。 | Apache-2.0 | [README](https://github.com/pharmaverse/admiral/blob/main/README.md) / [利用条件](https://github.com/pharmaverse/admiral/blob/main/LICENSE.md) |
| [admiralonco](../catalog.md#admiralonco) | admiral を拡張し、がん臨床試験の腫瘍応答や生存時間の解析データを導出する R パッケージです。 | Apache-2.0 | [README](https://github.com/pharmaverse/admiralonco/blob/main/README.md) / [利用条件](https://github.com/pharmaverse/admiralonco/blob/main/LICENSE.md) |
| [admiralvaccine](../catalog.md#admiralvaccine) | admiral を拡張し、ワクチン臨床試験の解析データを導出する R パッケージです。 | Apache-2.0 | [README](https://github.com/pharmaverse/admiralvaccine/blob/main/README.md) / [利用条件](https://github.com/pharmaverse/admiralvaccine/blob/main/LICENSE.md) |
| [AESTETIK](../catalog.md#aestetik) | 空間トランスクリプトームと組織像を統合し、局所構造を反映した表現学習を行うツールです。 | MIT | [README](https://github.com/ratschlab/aestetik/blob/main/README.md) / [利用条件](https://github.com/ratschlab/aestetik/blob/main/LICENSE) |
| [alphabase](../catalog.md#alphabase) | ペプチド、修飾、スペクトルライブラリなどを AlphaPept 系ツールで共通に扱うライブラリです。 | Apache-2.0 | [README](https://github.com/MannLabs/alphabase/blob/main/README.md) / [利用条件](https://github.com/MannLabs/alphabase/blob/main/LICENSE.txt) |
| [alphadia](../catalog.md#alphadia) | DIA 質量分析データをスペクトルライブラリと転移学習により同定・定量するツールです。 | Apache-2.0 | [README](https://github.com/MannLabs/alphadia/blob/main/README.md) / [利用条件](https://github.com/MannLabs/alphadia/blob/main/LICENSE.txt) |
| [alphamap](../catalog.md#alphamap) | 質量分析で同定したペプチドをタンパク質配列上に注釈・可視化するツールです。 | Apache-2.0 | [README](https://github.com/MannLabs/alphamap/blob/main/README.md) / [利用条件](https://github.com/MannLabs/alphamap/blob/main/LICENSE) |
| [alphapeptdeep](../catalog.md#alphapeptdeep) | ペプチドの質量スペクトルや保持時間などを深層学習で予測するツールです。 | Apache-2.0 | [README](https://github.com/MannLabs/alphapeptdeep/blob/main/README.md) / [利用条件](https://github.com/MannLabs/alphapeptdeep/blob/main/LICENSE.txt) |
| [alphapeptstats](../catalog.md#alphapeptstats) | 質量分析によるタンパク質定量結果に前処理、統計解析、可視化を適用するツールです。 | Apache-2.0 | [README](https://github.com/MannLabs/alphapeptstats/blob/main/README.md) / [利用条件](https://github.com/MannLabs/alphapeptstats/blob/main/LICENSE.txt) |
| [alphaquant](../catalog.md#alphaquant) | 質量分析によるペプチドとタンパク質の定量解析を行うツールです。 | Apache-2.0 | [README](https://github.com/MannLabs/alphaquant/blob/main/README.md) / [利用条件](https://github.com/MannLabs/alphaquant/blob/main/LICENSE) |
| [alphatims](../catalog.md#alphatims) | timsTOF 質量分析データの多次元信号を読み込み、抽出・可視化するライブラリです。 | Apache-2.0 | [README](https://github.com/MannLabs/alphatims/blob/main/README.md) / [利用条件](https://github.com/MannLabs/alphatims/blob/main/LICENSE.txt) |
| [AmbiDose](../catalog.md#ambidose) | 液滴型 single-cell RNA-seq の環境 RNA 混入を推定し、発現カウントを補正するツールです。 | Apache-2.0 | [README](https://github.com/leelieber2025/AmbiDose/blob/main/README.md) / [利用条件](https://github.com/leelieber2025/AmbiDose/blob/main/LICENSE) |
| [AMICI](../catalog.md#amici) | 生物学の常微分方程式モデルに感度解析とパラメータ推定向け計算を提供するライブラリです。 | BSD-3-Clause | [README](https://github.com/AMICI-dev/AMICI/blob/main/README.md) / [利用条件](https://github.com/AMICI-dev/AMICI/blob/main/LICENSE.md) |
| [annsel](../catalog.md#annsel) | AnnData に対して選択、フィルタリング、グループ化などの表形式操作を提供するライブラリです。 | MIT | [README](https://github.com/srivarra/annsel/blob/main/README.md) / [利用条件](https://github.com/srivarra/annsel/blob/main/LICENSE) |
| [AnnZarro](../catalog.md#annzarro) | AnnData の細胞・遺伝子行列をブラウザ上で連動表示する読み取り専用ビューアです。 | MIT | [README](https://github.com/settylab/annzarro/blob/main/README.md) / [利用条件](https://github.com/settylab/annzarro/blob/main/LICENSE) |
| [ATLAS single-cell](../catalog.md#atlas-single-cell) | 単一細胞の RNA と ATAC データを統合し、調節動態を考慮した細胞軌道を推定するツールです。 | BSD-3-Clause | [README](https://github.com/smilies-polito/atlas-smilies/blob/public/README.md) / [利用条件](https://github.com/smilies-polito/atlas-smilies/blob/public/LICENSE) |
| [benGRN](../catalog.md#bengrn) | 単一細胞データから推定した遺伝子ネットワークを参照ネットワークと比較評価するツールです。 | MIT | [README](https://github.com/jkobject/benGRN/blob/main/README.md) / [利用条件](https://github.com/jkobject/benGRN/blob/main/LICENSE) |
| [bento-tools](../catalog.md#bento-tools) | 空間トランスクリプトームの分子位置を細胞内スケールで解析するツールです。 | BSD-2-Clause | [README](https://github.com/YeoLab/bento-tools/blob/master/README.md) / [利用条件](https://github.com/YeoLab/bento-tools/blob/master/LICENSE) |
| [biolord](../catalog.md#biolord) | single-cell データの既知属性と未知変動を分離した潜在表現を学習するツールです。 | BSD-3-Clause | [README](https://github.com/nitzanlab/biolord/blob/main/README.md) / [利用条件](https://github.com/nitzanlab/biolord/blob/main/LICENSE) |
| [biorbd](../catalog.md#biorbd) | 人体の剛体・筋骨格モデルを用いて運動学と動力学を計算するライブラリです。 | MIT | [README](https://github.com/pyomeca/biorbd/blob/master/README.md) / [利用条件](https://github.com/pyomeca/biorbd/blob/master/LICENSE) |
| [BioSimulators Utils](../catalog.md#biosimulators-utils) | 生体モデルのシミュレータに共通 CLI、COMBINE archive、SED-ML 入出力を実装するためのライブラリです。 | MIT | [README](https://github.com/biosimulators/Biosimulators_utils/blob/dev/README.md) / [利用条件](https://github.com/biosimulators/Biosimulators_utils/blob/dev/LICENSE) |
| [CDISC CORE](../catalog.md#cdisc-core) | CDISC の適合性規則に基づいて臨床データを検証する CORE エンジンです。 | MIT | [README](https://github.com/cdisc-org/cdisc-rules-engine/blob/main/README.md) / [利用条件](https://github.com/cdisc-org/cdisc-rules-engine/blob/main/LICENSE) |
| [Cell_BLAST](../catalog.md#cell-blast) | 単一細胞発現プロファイルを参照データに照会し、対応する細胞集団を探索するツールです。 | MIT | [README](https://github.com/gao-lab/Cell_BLAST/blob/master/README.md) / [利用条件](https://github.com/gao-lab/Cell_BLAST/blob/master/LICENSE) |
| [CellAnnotator](../catalog.md#cellannotator) | 大規模言語モデルと事前知識を使い、single-cell RNA-seq の細胞型ラベル付けを支援するツールです。 | MIT | [README](https://github.com/quadbio/cell-annotator/blob/main/README.md) / [利用条件](https://github.com/quadbio/cell-annotator/blob/main/LICENSE) |
| [CellMapper](../catalog.md#cellmapper) | 参照 single-cell データから近傍探索によって細胞ラベルや発現量を転写するツールです。 | MIT | [README](https://github.com/quadbio/cellmapper/blob/main/README.md) / [利用条件](https://github.com/quadbio/cellmapper/blob/main/LICENSE) |
| [Cirrocumulus](../catalog.md#cirrocumulus) | 大規模な single-cell genomics データを対話的に可視化するブラウザ型ツールです。 | BSD-3-Clause | [README](https://github.com/lilab-bcb/cirrocumulus/blob/main/README.rst) / [利用条件](https://github.com/lilab-bcb/cirrocumulus/blob/main/LICENSE) |
| [cobrapy](../catalog.md#cobrapy) | 代謝ネットワークにフラックスバランス解析などの制約ベース解析を適用する Python ライブラリです。 | GPL-2.0 | [README](https://github.com/opencobra/cobrapy/blob/devel/README.rst) / [利用条件](https://github.com/opencobra/cobrapy/blob/devel/LICENSE) |
| [cobratoolbox](../catalog.md#cobratoolbox) | 代謝ネットワークの再構築と制約ベース解析を MATLAB で行うツールボックスです。 | GPL-3.0 | [README](https://github.com/opencobra/cobratoolbox/blob/master/README.rst) / [利用条件](https://github.com/opencobra/cobratoolbox/blob/master/LICENSE.md) |
| [COPASI](../catalog.md#copasi) | 生化学反応ネットワークを決定論的・確率的モデルでシミュレーションし、パラメータを推定するツールです。 | Artistic-2.0 | [README](https://github.com/copasi/COPASI/blob/develop/README.md) / [利用条件](https://github.com/copasi/COPASI/blob/develop/license.txt) |
| [corneto](../catalog.md#corneto) | 事前知識ネットワークとオミクス観測から制約付き最適化で生物学的ネットワークを推定するライブラリです。 | GPL-3.0 | [README](https://github.com/saezlab/corneto/blob/main/README.md) / [利用条件](https://github.com/saezlab/corneto/blob/main/LICENSE) |
| [cuspa](../catalog.md#cuspa) | 空間オミクスの点と領域の対応付けや細胞単位集約を GPU 上で処理するライブラリです。 | Apache-2.0 | [README](https://github.com/NVIDIA/cuspa/blob/main/README.md) / [利用条件](https://github.com/NVIDIA/cuspa/blob/main/LICENSE) |
| [dandelion](../catalog.md#dandelion) | 単一細胞 BCR・TCR 配列の前処理、クローン構造、発現データとの統合解析を行うツールです。 | AGPL-3.0 | [README](https://github.com/zktuong/dandelion/blob/master/README.md) / [利用条件](https://github.com/zktuong/dandelion/blob/master/LICENSE) |
| [delnx](../catalog.md#delnx) | 大規模 single-cell データの差次的発現を GPU を用いた回帰モデルで解析するツールです。 | MIT | [README](https://github.com/mlbelab/delnx/blob/main/README.md) / [利用条件](https://github.com/mlbelab/delnx/blob/main/LICENSE) |
| [directlfq](../catalog.md#directlfq) | 質量分析のペプチド・タンパク質シグナルからラベルフリー定量を行うツールです。 | Apache-2.0 | [README](https://github.com/MannLabs/directlfq/blob/main/README.md) / [利用条件](https://github.com/MannLabs/directlfq/blob/main/LICENSE) |
| [DisVoice](../catalog.md#disvoice) | 音声から発声、構音、韻律などの特徴を抽出する研究用ツールです。 | MIT | [README](https://github.com/jcvasquezc/DisVoice/blob/master/README.md) / [利用条件](https://github.com/jcvasquezc/DisVoice/blob/master/LICENSE) |
| [DOTools_py](../catalog.md#dotools-py) | single-cell RNA-seq の代表的な解析工程と可視化を Python からまとめて扱うツールです。 | MIT | [README](https://github.com/davidrm-bio/DOTools_py/blob/main/README.md) / [利用条件](https://github.com/davidrm-bio/DOTools_py/blob/main/LICENSE) |
| [DRVI](../catalog.md#drvi) | 単一細胞オミクスの潜在表現を分離し、細胞の異質性とデータ統合を解析するツールです。 | BSD-3-Clause | [README](https://github.com/theislab/DRVI/blob/main/README.md) / [利用条件](https://github.com/theislab/DRVI/blob/main/LICENSE) |
| [dvp-io](../catalog.md#dvp-io) | Deep Visual Proteomics のデータを SpatialData と相互変換する入出力ライブラリです。 | Apache-2.0 | [README](https://github.com/MannLabs/dvp-io/blob/main/README.md) / [利用条件](https://github.com/MannLabs/dvp-io/blob/main/LICENSE) |
| [eschr](../catalog.md#eschr) | 単一細胞データのクラスタリングを複数結果の統合と不確実性評価によって行うツールです。 | MIT | [README](https://github.com/zunderlab/eschr/blob/main/README.md) / [利用条件](https://github.com/zunderlab/eschr/blob/main/LICENSE) |
| [ezc3d](../catalog.md#ezc3d) | モーションキャプチャの C3D ファイルを C++・Python・MATLAB で読み書きするライブラリです。 | MIT | [README](https://github.com/pyomeca/ezc3d/blob/dev/README.md) / [利用条件](https://github.com/pyomeca/ezc3d/blob/dev/LICENSE) |
| [fava](../catalog.md#fava) | single-cell 発現やプロテオミクスから変分オートエンコーダで機能的関連を推定するツールです。 | MIT | [README](https://github.com/mikelkou/fava/blob/main/README.md) / [利用条件](https://github.com/mikelkou/fava/blob/main/LICENSE) |
| [flashdeconv](../catalog.md#flashdeconv) | 大規模な空間トランスクリプトームに対して細胞型デコンボリューションを行うツールです。 | BSD-3-Clause | [README](https://github.com/cafferychen777/flashdeconv/blob/main/README.md) / [利用条件](https://github.com/cafferychen777/flashdeconv/blob/main/LICENSE) |
| [FlowSOM Python](../catalog.md#flowsom-python) | 高次元サイトメトリーデータを自己組織化マップで分類・可視化する FlowSOM の Python 実装です。 | GPL-3.0 | [README](https://github.com/saeyslab/FlowSOM_Python/blob/main/README.md) / [利用条件](https://github.com/saeyslab/FlowSOM_Python/blob/main/LICENSE) |
| [GA4GH VRS Python](../catalog.md#ga4gh-vrs-python) | GA4GH Variation Representation Specification の変異表現と識別子計算を実装する Python ライブラリです。 | Apache-2.0 | [README](https://github.com/ga4gh/vrs-python/blob/main/README.md) / [利用条件](https://github.com/ga4gh/vrs-python/blob/main/LICENSE) |
| [GPTBioInsightor](../catalog.md#gptbioinsightor) | single-cell の細胞型注釈や機能解釈を大規模言語モデルで補助するツールです。 | BSD-3-Clause | [README](https://github.com/huang-sh/GPTBioInsightor/blob/main/README.md) / [利用条件](https://github.com/huang-sh/GPTBioInsightor/blob/main/LICENSE) |
| [grassp](../catalog.md#grassp) | 細胞内局在プロテオミクスをグラフに基づいて解析する Python ツールです。 | BSD-3-Clause | [README](https://github.com/czbiohub-sf/grassp/blob/main/README.md) / [利用条件](https://github.com/czbiohub-sf/grassp/blob/main/LICENSE) |
| [GRnnData](../catalog.md#grnndata) | 遺伝子調節ネットワークを AnnData と対応付けて保存・操作するデータ構造です。 | MIT | [README](https://github.com/cantinilab/GRnnData/blob/main/README.md) / [利用条件](https://github.com/cantinilab/GRnnData/blob/main/LICENSE) |
| [gsDesign](../catalog.md#gsdesign) | 群逐次臨床試験の境界、必要症例数、検出力を計算する R パッケージです。 | GPL-3.0 | [README](https://github.com/keaven/gsDesign/blob/master/README.md) / [利用条件](https://github.com/keaven/gsDesign/blob/master/LICENSE.md) |
| [gssnng](../catalog.md#gssnng) | 近傍グラフで平滑化した single-cell 発現データから遺伝子セットスコアを計算するツールです。 | MIT | [README](https://github.com/IlyaLab/gssnng/blob/main/README.md) / [利用条件](https://github.com/IlyaLab/gssnng/blob/main/LICENSE) |
| [gtsummary](../catalog.md#gtsummary) | 患者背景、解析結果、回帰モデルを報告用の統計表にまとめる R パッケージです。 | MIT | [README](https://github.com/ddsjoberg/gtsummary/blob/main/README.md) / [利用条件](https://github.com/ddsjoberg/gtsummary/blob/main/LICENSE.md) |
| [harpy](../catalog.md#harpy) | 空間 multi-omics の画像前処理から分割、SpatialData・AnnData による解析までを扱うツールです。 | BSD-3-Clause | [README](https://github.com/saeyslab/harpy/blob/main/README.md) / [利用条件](https://github.com/saeyslab/harpy/blob/main/LICENSE) |
| [HED Python](../catalog.md#hed-python) | BIDS などの HED 注釈を検証、要約、変換する Python ライブラリです。 | MIT | [README](https://github.com/hed-standard/hed-python/blob/main/README.md) / [利用条件](https://github.com/hed-standard/hed-python/blob/main/LICENSE) |
| [HED Specification](../catalog.md#hed-specification) | ヒト神経・行動実験のイベントや条件を階層語彙で注釈する HED の仕様です。 | CC-BY-4.0 | [README](https://github.com/hed-standard/hed-specification/blob/main/README.md) / [利用条件](https://github.com/hed-standard/hed-specification/blob/main/LICENSE) |
| [hotspot](../catalog.md#hotspot) | single-cell データの局所相関から情報を持つ遺伝子と遺伝子モジュールを抽出するツールです。 | MIT | [README](https://github.com/YosefLab/Hotspot/blob/master/README.md) / [利用条件](https://github.com/YosefLab/Hotspot/blob/master/LICENSE) |
| [illico](../catalog.md#illico) | single-cell RNA-seq の差次的発現を CPU 上の Wilcoxon 検定で処理するツールです。 | Apache-2.0 | [README](https://github.com/remydubois/illico/blob/main/README.md) / [利用条件](https://github.com/remydubois/illico/blob/main/LICENSE) |
| [infercnvpy](../catalog.md#infercnvpy) | single-cell RNA-seq の発現パターンからコピー数変化を推定する Scanpy 連携ツールです。 | BSD-3-Clause | [README](https://github.com/icbi-lab/infercnvpy/blob/main/README.md) / [利用条件](https://github.com/icbi-lab/infercnvpy/blob/main/LICENSE) |
| [kineticstoolkit](../catalog.md#kineticstoolkit) | 人体運動の計測データに座標変換、時系列処理、可視化を適用するツールキットです。 | Apache-2.0 | [README](https://github.com/kineticstoolkit/kineticstoolkit/blob/main/README.md) / [利用条件](https://github.com/kineticstoolkit/kineticstoolkit/blob/main/LICENSE.txt) |
| [kompot](../catalog.md#kompot) | 複数条件の single-cell データを連続的な細胞状態に沿って比較する統計解析ツールです。 | GPL-3.0 | [README](https://github.com/settylab/kompot/blob/main/README.md) / [利用条件](https://github.com/settylab/kompot/blob/main/LICENSE) |
| [LazySlide](../catalog.md#lazyslide) | 病理全スライド画像の読み込み、領域分割、特徴抽出を scverse と連携して行うツールです。 | MIT | [README](https://github.com/rendeirolab/LazySlide/blob/main/README.md) / [利用条件](https://github.com/rendeirolab/LazySlide/blob/main/LICENSE) |
| [libcellml](../catalog.md#libcellml) | 生理モデル記述形式 CellML を読み込み、検証、変換するライブラリです。 | Apache-2.0 | [README](https://github.com/cellml/libcellml/blob/main/README.rst) / [利用条件](https://github.com/cellml/libcellml/blob/main/LICENSE) |
| [libOpenCOR](../catalog.md#libopencor) | CellML 生理モデルの編集、検証、シミュレーションを支える OpenCOR のライブラリです。 | Apache-2.0 | [README](https://github.com/opencor/libopencor/blob/main/README.md) / [利用条件](https://github.com/opencor/libopencor/blob/main/LICENSE.txt) |
| [libRoadRunner](../catalog.md#roadrunner) | SBML 形式の生化学モデルを数値シミュレーションするライブラリです。 | Apache-2.0 | [README](https://github.com/sys-bio/roadrunner/blob/develop/README.md) / [利用条件](https://github.com/sys-bio/roadrunner/blob/develop/LICENSE.txt) |
| [libsbml](../catalog.md#libsbml) | Systems Biology Markup Language のモデルを読み書きし、検証・操作するライブラリです。 | LGPL-2.1 | [README](https://github.com/sbmlteam/libsbml/blob/development/README.md) / [利用条件](https://github.com/sbmlteam/libsbml/blob/development/LICENSE.html) |
| [mantispy](../catalog.md#mantispy) | Cell Painting の画像由来プロファイルに品質管理、正規化、バッチ補正を適用するツールです。 | BSD-3-Clause | [README](https://github.com/scverse/mantispy/blob/main/README.md) / [利用条件](https://github.com/scverse/mantispy/blob/main/LICENSE) |
| [Marsilea](../catalog.md#marsilea) | オミクスのヒートマップや oncoprint を注釈パネルと整列させて構成する可視化ライブラリです。 | MIT | [README](https://github.com/Marsilea-viz/marsilea/blob/main/README.md) / [利用条件](https://github.com/Marsilea-viz/marsilea/blob/main/LICENSE) |
| [maxspin](../catalog.md#maxspin) | 情報理論に基づいて空間トランスクリプトームの変動遺伝子を検出するツールです。 | MIT | [README](https://github.com/dcjones/maxspin/blob/main/README.md) / [利用条件](https://github.com/dcjones/maxspin/blob/main/LICENCE.md) |
| [metatools](../catalog.md#metatools) | 臨床試験のメタデータ定義を使って解析データセットの作成と整合性確認を行う R パッケージです。 | MIT | [README](https://github.com/pharmaverse/metatools/blob/main/README.md) / [利用条件](https://github.com/pharmaverse/metatools/blob/main/LICENSE.md) |
| [mmrm](../catalog.md#mmrm) | 臨床試験の反復測定アウトカムに混合効果モデルを適用する R パッケージです。 | Apache-2.0 | [README](https://github.com/openpharma/mmrm/blob/main/README.md) / [利用条件](https://github.com/openpharma/mmrm/blob/main/DESCRIPTION) |
| [Mowgli](../catalog.md#mowgli) | 対応のある single-cell multi-omics を最適輸送と非負行列分解で統合するツールです。 | GPL-3.0 | [README](https://github.com/cantinilab/Mowgli/blob/main/README.md) / [利用条件](https://github.com/cantinilab/Mowgli/blob/main/LICENSE) |
| [mrgsolve](../catalog.md#mrgsolve) | 薬物動態・薬力学などの常微分方程式モデルを R と C++ でシミュレーションするツールです。 | GPL-2.0 | [README](https://github.com/metrumresearchgroup/mrgsolve/blob/main/README.md) / [利用条件](https://github.com/metrumresearchgroup/mrgsolve/blob/main/LICENSE.md) |
| [Multivelo](../catalog.md#multivelo) | RNA とクロマチンアクセシビリティから細胞状態の時間的変化を推定するツールです。 | BSD-3-Clause | [README](https://github.com/welch-lab/MultiVelo/blob/main/README.rst) / [利用条件](https://github.com/welch-lab/MultiVelo/blob/main/LICENSE) |
| [ncountr](../catalog.md#ncountr) | NanoString nCounter の RCC ファイルに品質管理、正規化、差次的発現解析を適用するツールです。 | MIT | [README](https://github.com/princello/ncountr/blob/main/README.md) / [利用条件](https://github.com/princello/ncountr/blob/main/LICENSE) |
| [NeuroML 2](../catalog.md#neuroml2) | 神経細胞や神経回路の計算モデルを共通形式で記述する NeuroML 2 の仕様です。 | LGPL-3.0 | [README](https://github.com/NeuroML/NeuroML2/blob/master/README.md) / [利用条件](https://github.com/NeuroML/NeuroML2/blob/master/LICENSE.lesser) |
| [NicheNetPy](../catalog.md#nichenetpy) | ヒトやマウスの発現データと事前ネットワークから細胞間シグナル伝達を推定するツールです。 | BSD-3-Clause | [README](https://github.com/saeyslab/nichenetpy/blob/main/README.md) / [利用条件](https://github.com/saeyslab/nichenetpy/blob/main/LICENSE) |
| [nichepca](../catalog.md#nichepca) | 空間トランスクリプトームの近傍構成から主成分分析で組織領域を推定するツールです。 | MIT | [README](https://github.com/imsb-uke/nichepca/blob/main/README.md) / [利用条件](https://github.com/imsb-uke/nichepca/blob/main/LICENSE) |
| [nlmixr2](../catalog.md#nlmixr2) | 薬物動態・薬力学データに非線形混合効果モデルを当てはめる R ツールです。 | GPL-3.0 | [README](https://github.com/nlmixr2/nlmixr2/blob/main/README.md) / [利用条件](https://github.com/nlmixr2/nlmixr2/blob/main/LICENSE.md) |
| [novae](../catalog.md#novae) | 空間トランスクリプトームのグラフ表現から空間領域推定やバッチ補正を行うモデルです。 | BSD-3-Clause | [README](https://github.com/prism-oncology/novae/blob/main/README.md) / [利用条件](https://github.com/prism-oncology/novae/blob/main/LICENSE) |
| [omicverse](../catalog.md#omicverse) | bulk・single-cell を含むオミクス解析と可視化を統合する Python ツールキットです。 | GPL-3.0 | [README](https://github.com/omicverse/omicverse/blob/master/README.md) / [利用条件](https://github.com/omicverse/omicverse/blob/master/LICENSE) |
| [omnipath](../catalog.md#omnipath) | OmniPath のシグナル伝達・相互作用知識を取得し、オミクス解析に利用する Python クライアントです。 | MIT | [README](https://github.com/saezlab/omnipath/blob/main/README.rst) / [利用条件](https://github.com/saezlab/omnipath/blob/main/LICENSE) |
| [openMINDS](../catalog.md#openminds) | 神経科学のデータ、モデル、研究成果を関連付けて記述するメタデータスキーマです。 | MIT | [README](https://github.com/openMetadataInitiative/openMINDS/blob/main/README.md) / [利用条件](https://github.com/openMetadataInitiative/openMINDS/blob/main/LICENSE) |
| [Panpipes](../catalog.md#panpipes) | single-cell multi-omics と空間トランスクリプトームの解析工程を実行するワークフローです。 | BSD-3-Clause | [README](https://github.com/DendrouLab/panpipes/blob/main/README.md) / [利用条件](https://github.com/DendrouLab/panpipes/blob/main/LICENSE) |
| [Parselmouth](../catalog.md#parselmouth) | Praat の音声解析機能を Python から呼び出し、ピッチやフォルマントなどを計測するライブラリです。 | GPL-3.0 | [README](https://github.com/YannickJadoul/Parselmouth/blob/master/README.md) / [利用条件](https://github.com/YannickJadoul/Parselmouth/blob/master/LICENSE) |
| [ParTIpy](../catalog.md#partipy) | single-cell や空間オミクスの細胞状態をパレート最適性とアーキタイプ解析で整理するツールです。 | GPL-3.0 | [README](https://github.com/saezlab/ParTIpy/blob/main/README.md) / [利用条件](https://github.com/saezlab/ParTIpy/blob/main/LICENSE) |
| [PEAKQC](../catalog.md#peakqc) | single-cell ATAC-seq の断片長周期性を使ってデータ品質を評価するツールです。 | MIT | [README](https://github.com/loosolab/PEAKQC/blob/main/README.md) / [利用条件](https://github.com/loosolab/PEAKQC/blob/main/LICENSE) |
| [phenopacket-tools](../catalog.md#phenopacket-tools) | GA4GH Phenopackets の作成、形式変換、検証を行う Java ライブラリと CLI です。 | GPL-3.0 | [README](https://github.com/phenopackets/phenopacket-tools/blob/main/README.md) / [利用条件](https://github.com/phenopackets/phenopacket-tools/blob/main/LICENSE) |
| [PILOT](../catalog.md#pilot) | single-cell と病理画像の特徴から患者間の距離や変動を最適輸送で解析するツールです。 | MIT | [README](https://github.com/CostaLab/PILOT/blob/main/README.md) / [利用条件](https://github.com/CostaLab/PILOT/blob/main/LICENSE) |
| [popV](../catalog.md#popv) | 複数の細胞型注釈方法を統合し、参照データからのラベル転写に一致度を付けるツールです。 | MIT | [README](https://github.com/YosefLab/popV/blob/main/README.md) / [利用条件](https://github.com/YosefLab/popV/blob/main/LICENSE) |
| [Praat](../catalog.md#praat) | 音声のピッチ、フォルマント、強度、声質を計測・注釈する音声学ツールです。 | GPL-3.0-or-later | [README](https://github.com/praat/praat.github.io/blob/master/README.md) / [利用条件](https://github.com/praat/praat.github.io/blob/master/README.md) |
| [PupilMetrics](../catalog.md#pupilmetrics) | 瞳孔計測データの前処理とアウトカム指標の抽出を行うツールです。 | GPL-3.0 | [README](https://github.com/JulesGoninRIO/PupilMetrics/blob/main/README.md) / [利用条件](https://github.com/JulesGoninRIO/PupilMetrics/blob/main/LICENSE) |
| [pycea](../catalog.md#pycea) | single-cell lineage tracing の系譜構造を解析・可視化する Python ツールです。 | BSD-3-Clause | [README](https://github.com/YosefLab/pycea/blob/main/README.md) / [利用条件](https://github.com/YosefLab/pycea/blob/main/LICENSE) |
| [pychromVAR](../catalog.md#pychromvar) | single-cell ATAC-seq から転写因子モチーフのアクセシビリティ変動を評価する Python 実装です。 | MIT | [README](https://github.com/pinellolab/pychromVAR/blob/main/README.md) / [利用条件](https://github.com/pinellolab/pychromVAR/blob/main/LICENSE) |
| [pyCrossTalkeR](../catalog.md#pycrosstalker) | リガンド・受容体ネットワークから条件間の細胞間コミュニケーション変化を解析するツールです。 | MIT | [README](https://github.com/CostaLab/pyCrossTalkeR/blob/main/README.md) / [利用条件](https://github.com/CostaLab/pyCrossTalkeR/blob/main/LICENSE) |
| [pyLemur](../catalog.md#pylemur) | 複数条件の single-cell RNA-seq に対して LEMUR による潜在表現と比較解析を行う Python 実装です。 | MIT | [README](https://github.com/const-ae/pyLemur/blob/main/README.md) / [利用条件](https://github.com/const-ae/pyLemur/blob/main/LICENSE) |
| [pyomeca](../catalog.md#pyomeca) | 筋骨格計測の時系列や座標データを読み込み、信号処理と運動解析を行うライブラリです。 | Apache-2.0 | [README](https://github.com/pyomeca/pyomeca/blob/master/README.md) / [利用条件](https://github.com/pyomeca/pyomeca/blob/master/LICENSE.md) |
| [pypath](../catalog.md#pypath) | 生体分子の相互作用、複合体、注釈などの事前知識を統合する Python ライブラリです。 | GPL-3.0 | [README](https://github.com/saezlab/pypath/blob/master/README.rst) / [利用条件](https://github.com/saezlab/pypath/blob/master/LICENSE) |
| [pypillometry](../catalog.md#pypillometry) | 瞳孔径と視線の時系列に瞬目処理、イベント関連解析、可視化を適用するツールです。 | MIT | [README](https://github.com/ihrke/pypillometry/blob/master/README.md) / [利用条件](https://github.com/ihrke/pypillometry/blob/master/LICENSE) |
| [pysb](../catalog.md#pysb) | 生化学反応ネットワークを Python の規則で構成し、シミュレーションへつなぐライブラリです。 | BSD-2-Clause | [README](https://github.com/pysb/pysb/blob/master/README.rst) / [利用条件](https://github.com/pysb/pysb/blob/master/LICENSE.txt) |
| [pytximport](../catalog.md#pytximport) | RNA-seq の転写産物定量結果を読み込み、遺伝子単位に集約する tximport の Python 実装です。 | GPL-3.0 | [README](https://github.com/complextissue/pytximport/blob/main/README.md) / [利用条件](https://github.com/complextissue/pytximport/blob/main/LICENSE) |
| [pyUCell](../catalog.md#pyucell) | 単一細胞の遺伝子発現順位に基づいて遺伝子シグネチャスコアを計算するツールです。 | MIT | [README](https://github.com/carmonalab/pyucell/blob/master/README.md) / [利用条件](https://github.com/carmonalab/pyucell/blob/master/LICENSE) |
| [rbmi](../catalog.md#rbmi) | 臨床試験の欠測アウトカムに参照群ベースの多重代入を適用する R パッケージです。 | Apache-2.0 | [README](https://github.com/openpharma/rbmi/blob/main/README.md) / [利用条件](https://github.com/openpharma/rbmi/blob/main/LICENSE.md) |
| [Rectangle](../catalog.md#rectangle) | 混合発現データから細胞型構成を階層的に推定するデコンボリューションツールです。 | BSD-3-Clause | [README](https://github.com/ComputationalBiomedicineGroup/Rectangle/blob/main/README.md) / [利用条件](https://github.com/ComputationalBiomedicineGroup/Rectangle/blob/main/LICENSE) |
| [reproschema](../catalog.md#reproschema) | 質問紙や行動評価課題の構造と実施条件を再現可能に記述するスキーマです。 | Apache-2.0 (code); CC-BY-4.0 (documentation) | [README](https://github.com/ReproNim/reproschema/blob/main/README.md) / [利用条件](https://github.com/ReproNim/reproschema/blob/main/LICENSE) |
| [ReSurfEMG](../catalog.md#resurfemg) | 呼吸筋の表面筋電図に前処理、品質評価、特徴抽出を適用するライブラリです。 | Apache-2.0 | [README](https://github.com/resurfemg-org/ReSurfEMG/blob/main/README.md) / [利用条件](https://github.com/resurfemg-org/ReSurfEMG/blob/main/LICENSE) |
| [rpact](../catalog.md#rpact) | 確認的な逐次・適応的臨床試験のデザインと解析を支援する R パッケージです。 | LGPL-3.0 | [README](https://github.com/rpact-com/rpact/blob/main/README.md) / [利用条件](https://github.com/rpact-com/rpact/blob/main/LICENSE.md) |
| [rtables](../catalog.md#rtables) | 臨床試験の集計結果を階層的な報告表として構築する R パッケージです。 | Apache-2.0 | [README](https://github.com/pharmaverse/rtables/blob/main/README.md) / [利用条件](https://github.com/pharmaverse/rtables/blob/main/LICENSE) |
| [rxode2](../catalog.md#rxode2) | 薬物動態・薬力学などの常微分方程式モデルを R から定義し、シミュレーションするツールです。 | GPL-3.0 | [README](https://github.com/nlmixr2/rxode2/blob/main/README.md) / [利用条件](https://github.com/nlmixr2/rxode2/blob/main/LICENSE.md) |
| [SC2Spa](../catalog.md#sc2spa) | single-cell と空間発現データを学習し、細胞の空間位置を推定するツールです。 | BSD-3-Clause | [README](https://github.com/linbuliao/SC2Spa/blob/main/README.md) / [利用条件](https://github.com/linbuliao/SC2Spa/blob/main/LICENSE) |
| [SCALEX](../catalog.md#scalex) | single-cell RNA-seq や ATAC-seq を統合し、参照アトラスへの投影を行うツールです。 | BSD-3-Clause | [README](https://github.com/jsxlei/SCALEX/blob/main/README.md) / [利用条件](https://github.com/jsxlei/SCALEX/blob/main/LICENSE) |
| [scanpro](../catalog.md#scanpro) | single-cell データの細胞型比率を条件間で比較する統計解析ツールです。 | MIT | [README](https://github.com/loosolab/scanpro/blob/main/README.md) / [利用条件](https://github.com/loosolab/scanpro/blob/main/LICENSE) |
| [scATrans](../catalog.md#scatrans) | single-cell RNA-seq のスプライシング情報を用いて条件間の発現変化を補助的に解析するツールです。 | Apache-2.0 | [README](https://github.com/leelieber2025/scATrans/blob/main/README.md) / [利用条件](https://github.com/leelieber2025/scATrans/blob/main/LICENSE) |
| [scCellFie](../catalog.md#sccellfie) | single-cell と空間発現データから代謝タスクの活動を推定するツールです。 | MIT | [README](https://github.com/earmingol/scCellFie/blob/main/README.rst) / [利用条件](https://github.com/earmingol/scCellFie/blob/main/LICENSE.txt) |
| [scDataLoader](../catalog.md#scdataloader) | 大規模な単一細胞データベースからデータ取得、前処理、重み付きサンプリングを行うライブラリです。 | MIT | [README](https://github.com/jkobject/scDataLoader/blob/main/README.md) / [利用条件](https://github.com/jkobject/scDataLoader/blob/main/LICENSE) |
| [scFair](../catalog.md#scfair) | single-cell RNA-seq の高変動遺伝子選択にデータ適応的な基準を適用するツールです。 | Apache-2.0 | [README](https://github.com/leelieber2025/scFair/blob/main/README.md) / [利用条件](https://github.com/leelieber2025/scFair/blob/main/LICENSE) |
| [scGen](../catalog.md#scgen) | single-cell 発現データから細胞型や研究間の摂動応答を予測する生成モデルです。 | GPL-3.0 | [README](https://github.com/theislab/scgen/blob/master/README.md) / [利用条件](https://github.com/theislab/scgen/blob/master/LICENSE) |
| [schist](../catalog.md#schist) | single-cell データの細胞集団を確率的ブロックモデルで推定するツールです。 | BSD-3-Clause | [README](https://github.com/dawe/schist/blob/master/README.md) / [利用条件](https://github.com/dawe/schist/blob/master/LICENSE) |
| [scib-rapids](../catalog.md#scib-rapids) | single-cell データ統合の評価指標を RAPIDS により GPU 上で計算するツールです。 | BSD-3-Clause | [README](https://github.com/maarten-devries/scib-rapids/blob/main/README.md) / [利用条件](https://github.com/maarten-devries/scib-rapids/blob/main/LICENSE) |
| [scPRINT](../catalog.md#scprint) | single-cell 発現から遺伝子ネットワークを推定する基盤モデルです。 | GPL-3.0 | [README](https://github.com/cantinilab/scPRINT/blob/main/README.md) / [利用条件](https://github.com/cantinilab/scPRINT/blob/main/LICENSE) |
| [scPRINT-2](../catalog.md#scprint-2) | single-cell データの表現学習と遺伝子ネットワーク推定を行う scPRINT 系モデルです。 | GPL-3.0 | [README](https://github.com/cantinilab/scPRINT-2/blob/main/README.md) / [利用条件](https://github.com/cantinilab/scPRINT-2/blob/main/LICENSE) |
| [scTriangulate](../catalog.md#sctriangulate) | 異なるクラスタリング結果を照合し、single-cell の細胞集団分類を調整するツールです。 | MIT | [README](https://github.com/frankligy/scTriangulate/blob/main/README.md) / [利用条件](https://github.com/frankligy/scTriangulate/blob/main/LICENSE) |
| [scviva-tools](../catalog.md#scviva-tools) | 空間トランスクリプトームのニッチ表現学習、デコンボリューション、ノイズ補正を統合するツールです。 | BSD-3-Clause | [README](https://github.com/YosefLab/scviva-tools/blob/main/README.md) / [利用条件](https://github.com/YosefLab/scviva-tools/blob/main/LICENSE) |
| [scxmatch](../catalog.md#scxmatch) | single-cell データの二群間の分布変化を距離マッチングと cross-match 検定で評価するツールです。 | MIT | [README](https://github.com/bionetslab/scxmatch/blob/master/README.md) / [利用条件](https://github.com/bionetslab/scxmatch/blob/master/LICENSE) |
| [scXpand](../catalog.md#scxpand) | paired TCR データを使わず single-cell RNA-seq から T 細胞クローン増殖を推定するツールです。 | MIT | [README](https://github.com/yizhak-lab-ccg/scXpand/blob/main/README.md) / [利用条件](https://github.com/yizhak-lab-ccg/scXpand/blob/main/LICENSE) |
| [scyan](../catalog.md#scyan) | 生物学的知識を組み込んだ生成モデルでサイトメトリーデータの細胞型を注釈するツールです。 | BSD-3-Clause | [README](https://github.com/prism-oncology/scyan/blob/main/README.md) / [利用条件](https://github.com/prism-oncology/scyan/blob/main/LICENSE) |
| [sdtm.oak](../catalog.md#sdtm-oak) | 収集した臨床データをマッピング規則に基づいて CDISC SDTM 形式へ変換する R パッケージです。 | Apache-2.0 | [README](https://github.com/pharmaverse/sdtm.oak/blob/main/README.md) / [利用条件](https://github.com/pharmaverse/sdtm.oak/blob/main/LICENSE.md) |
| [sdtmchecks](../catalog.md#sdtmchecks) | CDISC SDTM データの解析前チェックを実行する R パッケージです。 | Apache-2.0 | [README](https://github.com/pharmaverse/sdtmchecks/blob/devel/README.md) / [利用条件](https://github.com/pharmaverse/sdtmchecks/blob/devel/LICENSE.md) |
| [sensormotion](../catalog.md#sensormotion) | 加速度センサーから身体活動や歩行の特徴を計算する Python ライブラリです。 | MIT | [README](https://github.com/thesimonho/sensormotion/blob/master/README.rst) / [利用条件](https://github.com/thesimonho/sensormotion/blob/master/LICENSE) |
| [sift-sc](../catalog.md#sift-sc) | 既知の生物学的変動を除いて single-cell データの残る構造を解析するツールです。 | BSD-3-Clause | [README](https://github.com/nitzanlab/sift-sc/blob/main/README.rst) / [利用条件](https://github.com/nitzanlab/sift-sc/blob/main/LICENSE) |
| [sincei](../catalog.md#sincei) | 単一細胞エピゲノムの BAM データからシグナル集約や解析を行う CLI・Python ツールです。 | MIT | [README](https://github.com/bhardwaj-lab/sincei/blob/master/README.md) / [利用条件](https://github.com/bhardwaj-lab/sincei/blob/master/LICENCE.txt) |
| [Sobolev Alignment](../catalog.md#sobolev-alignment) | 前臨床モデルと患者由来の single-cell プロファイルを確率モデルで比較するツールです。 | MIT | [README](https://github.com/NKI-CCB/sobolev_alignment/blob/main/README.md) / [利用条件](https://github.com/NKI-CCB/sobolev_alignment/blob/main/LICENSE) |
| [spatial-eggplant](../catalog.md#spatial-eggplant) | 複数の空間トランスクリプトームを共通座標系へ対応付けるツールです。 | MIT | [README](https://github.com/almaan/eggplant/blob/master/README.md) / [利用条件](https://github.com/almaan/eggplant/blob/master/LICENSE) |
| [spatialproteomics](../catalog.md#spatialproteomics) | 多重蛍光組織画像の領域分割、マーカー定量、空間解析を行うツールです。 | MIT | [README](https://github.com/sagar87/spatialproteomics/blob/main/README.md) / [利用条件](https://github.com/sagar87/spatialproteomics/blob/main/LICENSE) |
| [spatiomic](../catalog.md#spatiomic) | 空間プロテオミクスを画素クラスタリング、クラスタ量比較、空間統計で解析するライブラリです。 | Apache-2.0 | [README](https://github.com/complextissue/spatiomic/blob/main/README.md) / [利用条件](https://github.com/complextissue/spatiomic/blob/main/LICENSE) |
| [spm1d](../catalog.md#spm1d) | 歩行や運動学などの一次元連続波形に統計的パラメトリックマッピングを適用するライブラリです。 | GPL-3.0 | [README](https://github.com/spm1d-org/spm1d-v0.4/blob/master/README.md) / [利用条件](https://github.com/spm1d-org/spm1d-v0.4/blob/master/LICENSE.txt) |
| [STMiner](../catalog.md#stminer) | 遺伝子ごとの空間発現パターンから空間トランスクリプトームを解析するツールです。 | GPL-3.0 | [README](https://github.com/xjtu-omics/STMiner/blob/main/readme.md) / [利用条件](https://github.com/xjtu-omics/STMiner/blob/main/LICENSE) |
| [Symphonypy](../catalog.md#symphonypy) | 参照 single-cell データから Symphony アルゴリズムで細胞型ラベルを転写する Python 実装です。 | GPL-3.0 | [README](https://github.com/potulabe/symphonypy/blob/main/README.md) / [利用条件](https://github.com/potulabe/symphonypy/blob/main/LICENSE) |
| [TAU Community Detection](../catalog.md#tau-community-detection) | single-cell の近傍グラフを遺伝的探索と Leiden 法によってクラスタリングするツールです。 | MIT | [README](https://github.com/HillelCharbit/TAU/blob/master/README.md) / [利用条件](https://github.com/HillelCharbit/TAU/blob/master/LICENSE) |
| [teal](../catalog.md#teal) | 臨床試験データを対話的に探索する Shiny アプリを構築する R フレームワークです。 | Apache-2.0 | [README](https://github.com/pharmaverse/teal/blob/main/README.md) / [利用条件](https://github.com/pharmaverse/teal/blob/main/LICENSE) |
| [tellurium](../catalog.md#tellurium) | 生化学モデルの記述、シミュレーション、解析を統合した Python 環境です。 | Apache-2.0 | [README](https://github.com/sys-bio/tellurium/blob/develop/README.md) / [利用条件](https://github.com/sys-bio/tellurium/blob/develop/LICENSE.txt) |
| [tern](../catalog.md#tern) | 臨床試験の患者背景、有害事象、生存時間などの表・一覧・図を作成する R パッケージです。 | Apache-2.0 | [README](https://github.com/pharmaverse/tern/blob/main/README.md) / [利用条件](https://github.com/pharmaverse/tern/blob/main/LICENSE) |
| [TreeData](../catalog.md#treedata) | AnnData の細胞・特徴量に対応する木構造を保持し、系譜情報を扱うライブラリです。 | BSD-3-Clause | [README](https://github.com/YosefLab/treedata/blob/main/README.md) / [利用条件](https://github.com/YosefLab/treedata/blob/main/LICENSE) |
| [wsidata](../catalog.md#wsidata) | 病理全スライド画像と組織・タイル形状を SpatialData に基づいて管理するデータ構造です。 | MIT | [README](https://github.com/rendeirolab/wsidata/blob/main/README.md) / [利用条件](https://github.com/rendeirolab/wsidata/blob/main/LICENSE) |
| [xportr](../catalog.md#xportr) | CDISC SDTM・ADaM データの型や属性を整え、SAS XPT ファイルを書き出す R パッケージです。 | MIT | [README](https://github.com/atorus-research/xportr/blob/main/README.md) / [利用条件](https://github.com/atorus-research/xportr/blob/main/LICENSE.md) |

## 既存の移転・保守状態

移転先はGitHubが返した同一 repository identity を確認しています。IDは変えず、repo URLを更新しました。公式サイト全体の現行性を保証する点検ではありません。

| ID | 更新 | 現在のrepo |
| --- | --- | --- |
| `cellrank` | canonical repository URL | [scverse/cellrank](https://github.com/scverse/cellrank) |
| `decoupler` | canonical repository URL | [scverse/decoupler](https://github.com/scverse/decoupler) |
| `qiime2` | canonical repository URL | [rachis-org/rachis](https://github.com/rachis-org/rachis) |
| `biosppy` | archived warning | [PIA-Group/BioSPPy](https://github.com/PIA-Group/BioSPPy) |
| `medcat` | archived warning | [CogStack/MedCAT](https://github.com/CogStack/MedCAT) |
| `presidio` | canonical repository URL | [data-privacy-stack/presidio](https://github.com/data-privacy-stack/presidio) |
| `sirius` | canonical repository URL | [sirius-ms/sirius](https://github.com/sirius-ms/sirius) |
| `aicsimageio` | archived warning | [AllenCellModeling/aicsimageio](https://github.com/AllenCellModeling/aicsimageio) |
| `epinowcast` | canonical repository URL | [epinowcast/epinowcast](https://github.com/epinowcast/epinowcast) |
| `flower` | canonical repository URL | [flwrlabs/flower](https://github.com/flwrlabs/flower) |
| `tensorflow-federated` | canonical repository URL | [google-parfait/tensorflow-federated](https://github.com/google-parfait/tensorflow-federated) |
| `opacus` | canonical repository URL | [meta-pytorch/opacus](https://github.com/meta-pytorch/opacus) |
| `pyrosm` | canonical repository URL | [pyrosm/pyrosm](https://github.com/pyrosm/pyrosm) |
| `earthaccess` | canonical repository URL | [earthaccess-dev/earthaccess](https://github.com/earthaccess-dev/earthaccess) |
| `cardinal` | canonical repository URL | [Cardinalverse/Cardinal](https://github.com/Cardinalverse/Cardinal) |
| `scikit-digital-health` | canonical repository URL | [pfizer-opensource/scikit-digital-health](https://github.com/pfizer-opensource/scikit-digital-health) |
| `ga4gh-service-registry` | canonical repository URL | [ga4gh/ga4gh-service-registry](https://github.com/ga4gh/ga4gh-service-registry) |
| `vardictjava` | archived warning | [AstraZeneca-NGS/VarDictJava](https://github.com/AstraZeneca-NGS/VarDictJava) |
| `liana-py` | canonical repository URL | [scverse/liana](https://github.com/scverse/liana) |
| `sopa` | canonical repository URL | [prism-oncology/sopa](https://github.com/prism-oncology/sopa) |
| `r5r` | canonical repository URL | [ipea/r5r](https://github.com/ipea/r5r) |
| `hospitalrun` | archived warning | [HospitalRun/hospitalrun-frontend](https://github.com/HospitalRun/hospitalrun-frontend) |
| `pymovements` | canonical repository URL | [pymovements/pymovements](https://github.com/pymovements/pymovements) |
| `rioxarray` | canonical repository URL | [vylor/rioxarray](https://github.com/vylor/rioxarray) |
| `nf-core-callingcards` | archived warning | [nf-core/callingcards](https://github.com/nf-core/callingcards) |
| `ga4gh-gks-core` | canonical repository URL | [ga4gh/gkm-core](https://github.com/ga4gh/gkm-core) |

## 保留した新規候補

以下は削除された機能・失敗した導入ではなく、今回追加しなかった候補です。404はその探索URLの結果であり、プロジェクトそのものが不存在とは限りません。

| 候補 | 理由 | 一次情報 |
| --- | --- | --- |
| CellOracle | 非商用・学術目的限定の修正 Apache 条件。登録簿の Apache-2.0 表記を採用しません。 | [公式source](https://github.com/morris-lab/CellOracle) |
| clone2vec | MIT バッジはありますが、今回確認したルートにライセンス本文がなく保留。 | [公式source](https://github.com/kharchenkolab/clone2vec) |
| spatialdataR | 登録簿に Artistic-2.0 表記がありますが今回のライセンス一次証拠が不足。 | [公式source](https://github.com/HelenaLC/spatialdataR) |
| AlphaPeptTools | 開発中と明記されており成熟度の追加確認待ち。 | [公式source](https://github.com/MannLabs/alphapepttools) |
| alpharaw | Apache コードに加えて、非商用限定の SCIEX SDK 等の独自条件バイナリを同梱。単純な OSS としては採録せず保留。 | [公式source](https://github.com/MannLabs/alpharaw) |
| pyEDA | 公式リポジトリのライセンス一次証拠が不足。 | [公式source](https://github.com/HealthSciTech/pyEDA) |
| VoiceLab | README は MIT を宣言していますが参照する LICENSE 本文を今回確認できず保留。 | [公式source](https://github.com/Voice-Lab/VoiceLab) |
| Open-PupilEXT | 複数の組み込みライブラリと個別条件の詳細確認が残るため保留。 | [公式source](https://github.com/openPupil/Open-PupilEXT) |
| pyCGM2 | コードの指定条件が CC-BY-SA-4.0 のため OSS 用ライセンスと同一視せず保留。 | [公式source](https://github.com/pyCGM2/pyCGM2) |
| opencor | 旧 desktop repo が archived。現行 libOpenCOR を別途採録。 | [公式source](https://github.com/opencor/opencor) |
| sbml-specifications | 公開仕様を確認しましたがリポジトリ内の利用条件の詳細確認が残ります。 | [公式source](https://github.com/sbmlteam/sbml-specifications) |
| sed-ml | 公開仕様を確認しましたがリポジトリ内の利用条件の詳細確認が残ります。 | [公式source](https://github.com/SED-ML/sed-ml) |
| mattdotbat/gaitpy | 探索URLは不存在。正しい matt002/GaitPy は保守終了と明記され、収録済み scikit-digital-health を案内。 | [公式source](https://github.com/matt002/GaitPy) |
| pharmaverse/xportr | 探索URLは不存在。公式 atorus-research/xportr を確認して別途採録。 | [公式source](https://github.com/atorus-research/xportr) |
| Merck/gsDesign | 探索URLは不存在。公式 keaven/gsDesign を確認して別途採録。 | [公式source](https://github.com/keaven/gsDesign) |

登録簿の開発用テンプレート、運営文書、統計サイト、チュートリアル等も解析本体とは分けています。14項目の判定はJSONの `registry_screening` にあります。

## 未確認範囲と網羅性

**ネット上を調べ尽くした、または生体データ解析OSSを完全列挙したとは主張しません。** 今回は大きな既存台帳の全件メタデータ点検と、公式登録簿・不足領域を使った一巡の広い拡充です。終了条件は「選んだ公式登録簿の全件を判定し、採録候補の一次証拠と検証を揃えること」であり、全インターネットで新規候補がなくなったという意味ではありません。

- GitHub以外の121件は今回の全件repo API照合の対象外です。GitLab、Bioconductor git、CRAN 等を横断する個別の到達性・ライセンス本文点検が残ります。
- 既存1,105件のAPI確認は repo の存在・identity・移転・archived・ライセンス自動検出情報です。既存全件の README、全LICENSE本文、公式サイト、インストール、機能・性能の再評価はしていません。
- 既存API照合で279件は license が未検出または NOASSERTION でした。これは「無許諾」「非OSS」を意味しません。R DESCRIPTION、複合ライセンス、別ディレクトリにある条件等を個別確認するための優先候補です。
- Bioconductor の全パッケージ、CRAN全体、bio.tools、GitLab・SourceForge、医用画像の各拡張、地域固有の臨床ソフト、非英語プロジェクトの全件照合は未実施です。
- 多数のソフトを同一環境に導入して試験してはいません。ここでの実行検証はカタログ、CLI、生成ページ、索引、重複・証拠記録の検査です。
- 更新され続ける領域なので、採録の不足・URL変更・利用条件変更は今後も発生します。保留を未検証のまま採録するより、一次情報の確認を優先します。

## 品質検証

- `make catalog-page`: JSONから全件ページと分野・スケール索引を再生成。
- `make validate`: 必須項目、URL、ID、重複タグ、日付、正規化したrepoの重複を検証。
- `make test`: カタログ・CLI・一次証拠・件数・索引・回帰テスト。
- 生成を繰り返して差分がないことを確認し、README・ページ・元データの件数を一致させます。
- CIでも生成済みページと索引が元データに一致していることを確認します。

ローカル検証: `make validate`、`make test`（25テスト）、JSON Schema Draft 2020-12 の検証が成功しました。全件ページ・索引を再生成して一致を確認しています。最終commitのCI状態はPRに記載します。
