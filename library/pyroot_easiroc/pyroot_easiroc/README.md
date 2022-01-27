# TrackSeeker
TChainの派生クラス。Easirocで取れた測定データの読み込み, FittingによるThresholdの決定, Effeciencyの見積もりなどをする。

## class variables
- [channel 対応図](/docs/images/channel_image.jpeg)
- OUTER_CHNNELS: Set\[int]
    - 各ボードについているMPPCの上下4chずつ, 計16chが入っている
- INNER_CHANNELS: Set\[int]
    - 各ボードについているMPPCの上下4ch以外のch, 計48ch
- VERTICAL_GROUP_EAST_BOARD: Tuple[Tuple[int]]
    - 東ボードの鉛直座標が同じMPPCをtupleに詰めている
        ```
        (
            (0, 4, 8, 12, 16, 20, 24, 28),
            (1, 5, 9, 13, 17, 21, 25, 29),
            (2, 6, 10, 14, 18, 22, 26, 30),
            (3, 7, 11, 15, 19, 23, 27, 31)
        )
        ```
-  VERTICAL_GROUP_WEST_BOARD: Tuple[Tuple[int]]
    - 西ボードの鉛直座標が同じMPPCをtupleに詰めている
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

## Menber variables
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

### calc_effeciency(ch_target)
- ch_targetの検出効率を計算する
- 計算式
    ```
    (検出効率) = (ターゲットchと上下のchが鳴ったイベント数) / (上下のchが鳴ったイベント数)
    ```
- 上下16ch以外のchに対応している