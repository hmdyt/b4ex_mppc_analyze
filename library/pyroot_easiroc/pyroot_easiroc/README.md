# TrackSeeker
TChainの派生クラス。Easirocで取れた測定データの読み込み, FittingによるThresholdの決定, Effeciencyの見積もりなどをする。

## class variables
- [channel 対応図](/docs/images/channel_image.jpeg)
- OUTER_CHNNELS: Set\[int]
    - 各ボードについているMPPCの上下4chずつ, 計16chが入っている
- INNER_CHANNELS: Set\[int]
    - 各ボードについているMPPCの上下4ch以外のch, 計48ch
- VERTICAL_GROUP_EAST_BOARD: Tuple[Tuple[int]]
    - 東ボードの鉛直方向に垂直な座標が同じMPPCをtupleに詰めている
        ```
        (
            (0, 4, 8, 12, 16, 20, 24, 28),
            (1, 5, 9, 13, 17, 21, 25, 29),
            (2, 6, 10, 14, 18, 22, 26, 30),
            (3, 7, 11, 15, 19, 23, 27, 31)
        )
        ```
-  VERTICAL_GROUP_WEST_BOARD: Tuple[Tuple[int]]
    - 西ボードの鉛直方向に垂直な座標が同じMPPCをtupleに詰めている
        ```
        (
            (60, 56, 52, 48, 44, 40, 36, 32),
            (61, 57, 53, 49, 45, 41, 37, 33),
            (62, 58, 54, 50, 46, 42, 38, 34),
            (63, 59, 55, 51, 47, 43, 39, 35)
        )
        ```
- VERTICAL_GROUP: Tuple[Tuple[int]]
    - VERTICAL_GROUP_EAST_BOARD + VERTICAL_GROUP_WEST_BOARD

## Member variables
- \_n_event: int
    - 読み込んだrootfileの中の総エントリー数
- \_hist: List[TH1D]\(64)
    - VadcHigh\[64]のヒストグラム
- \__f_landau: List[TF1]\(64)
    - landau fittingに使用する関数
- \_is_hit: List[np.array(dtype=bool)]
    - thresholdによって決められた, チャンネルごとのヒット情報
    - len(\_is_hit) == \_n_event
    - \_is_hit[i].shape == (64, )
- \_effeciency: List[float]\(64)
    - 計算されたeffeciencyが格納される
    - 計算前はNoneが詰まっている

## Member functions
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

### calc_effeciency(ch_target)
- ch_targetの検出効率を計算する
- 計算式
    ```
    (検出効率) = (ターゲットchと上下のchが鳴ったイベント数) / (上下のchが鳴ったイベント数)
    ```
- 上下16ch以外のchに対応している

# HitArrayGen
測定ファイル(runxxx.root)からヒット情報を生成するためのクラス。
チャンネルごとにthreshold(ADC value)を設定し, generate_hit_arrayを実行することでヒット情報が生成される

## TODO
- \_hit_arrayをrootfileとして書き出せるようにする

## usage (example)
- run017の測定ファイルに対して, ずべてのチャンネルのthresholdをADC1500としてヒット情報を生成するなら以下のように書く
    ```python
    from pyroot_easiroc.HitArrayGen import HitArrayGen

    hit_array_gen = HitArrayGen("run017.root")
    for ch in range(64):
        hit_array_gen.set_threshold(ch, 1500)
    hit_array_gen.generate_hit_array()
    hit_array = hit_array_gen.get_hit_array()

    print(hit_array.shape)
    print(hit_array[0])# showing 0th event

    ```

## Class Variables
### CHANNELS_UPSIDE: np.array(List[List[int]])
- 井形に組んでいる上側シンチレータのchを格納している
``` 
array([
    [ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11],
    [12, 13, 14, 15],
    [16, 17, 18, 19],
    [20, 21, 22, 23],
    [24, 25, 26, 27],
    [28, 29, 30, 31]
    ])
```

### CHANNELS_DOWNSIDE: np.array(List[List[int]])
- 井形に組んでいる下側シンチレータのchを格納している
```
array([
    [63, 62, 61, 60],
    [59, 58, 57, 56],
    [55, 54, 53, 52],
    [51, 50, 49, 48],
    [47, 46, 45, 44],
    [43, 42, 41, 40],
    [39, 38, 37, 36],
    [35, 34, 33, 32]
    ])
```

## Member functions
### constructor(rootfile_path)
- コンストラクタで対象とするrootfileのパスを設定する
- 正規表現は使えない
- .rootで終わらないと怒られる
  
### set_threshold(ch: int, adc_th: int) -> void
- chごとのthreshold(ADC_value)を設定する
- 何も設定しないと, 全てのchでADC_value 1200になっている

### generate_hit_array() -> void
- 測定ファイルと設定されたthresholdの情報からヒット情報を計算する
- 計算結果であるヒット情報はメンバ変数_hit_arrayに格納されている

### get_hit_array() -> np.array(dtype=np.bool)
- ヒット情報 (_hit_array) を返す関数　ゲッタ

## _hit_arrayについて
- イベント数の長さだけ3次元arrayが格納されている
    - _hit_array.shape = (n_event, 8, 4, 4)
- 各インデックスの意味
    - i_event: 何番目のイベントか
    - k: 検出器のz軸方向
    - i,j: xy平面で検出器のどこにあるか
    ```
        _hit_array[i_event][k][i][j]
    ```
    |i,j|k|
    |---|---|
    |![xy](/docs/images/detector_index_xy.jpeg)|![zx](/docs/images/detector_index_zx.jpeg)|

# EffCalculator
検出効率を調べるためのクラス。

## constructor(n_hit, tree_name, filepath) -> None
- n_hit: 検出効率を調べるためのイベントの選定基準, 縦方向にn_hitよりも多くヒットしていれば検出効率の計算に使うイベントとする
- tree_name: 対象とするTTreeの名前
- filepath: 対象とするTTreeの入ったrootfileのパス

## determine_hits(adc_threshold_s: List[int]) -> None
- chごとのthreshold ADC valueをlistにして渡す
- thresholdを超えたか超えてないかを全ch, eventで決める

## get_64ch_effeciency() -> List[int]
- 現在の設定で検出効率を計算する
- chごとに計算された検出効率がreturnされる