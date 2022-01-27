# TrackSeeker
TChainの派生クラス。Easirocで取れた測定データの読み込み, FittingによるThresholdの決定, Effeciencyの見積もりなどをする。

## Menber variables
- \_n_event: int
    - 読み込んだrootfileの中の総エントリー数
- \_hist: List[TH1D]\(64)
    - VadcHigh\[64]のヒストグラム
- \__f_landau: List[TF1]\(64)
    - landau fittingに使用する関数


## Menber functions
### constructor(name, filepath)
- arg
    - name: treeの名前
    - filepath: rootfileの場所を指定, ワイルドカードに対応

### set_landau_fit_range(ch, fit_range_min, fit_range_max)
- 各チャンネルのヒストグラムをFitするときのFitting範囲を指定する。デフォルトでは全てのチャンネルがADC値1200 ~ 2700の範囲になっている

### fit_by_landau(ch)
- chごとにfittingを実行する

### save_hist()
- 64ch全てのヒストグラムをpngに書き出す