# 2026-11-27 ライセンス監査（4件）

現行正本（確認時 main `63a2f305d73b03da0d43611a141aee08df0381a1`）の未記入ライセンスを、開発元の一次資料に照合して補完した。収録件数は1370件のまま。データ・依存関係・運用サービスの利用条件を示すものではない。

| ID | 記録値 | 一次資料 | 対応Issue |
| --- | --- | --- | --- |
| `tidycensus` | MIT + file LICENSE | [開発元](https://github.com/walkerke/tidycensus/blob/master/DESCRIPTION) | #34 |
| `tmle3` | GPL-3 | [開発元](https://github.com/tlverse/tmle3/blob/master/DESCRIPTION) | #30 |
| `scverse-io` | BSD-3-Clause | [開発元](https://github.com/scverse/scverse-io/blob/main/LICENSE) | #28 |
| `ga4gh-data-connect` | Apache-2.0 | [開発元](https://github.com/ga4gh/data-connect/blob/develop/LICENSE) | #29 |

全件表の生成行を正本の全1370件と照合したうえで再生成し、分類タグは変更していないため分類索引の生成日を更新した。Python/Nodeのテストと公開サイト実表示はこの作業環境では未実行であり、PRのCI結果を別途確認する。残るライセンス・保守状態の監査Issueは本変更の対象外。
