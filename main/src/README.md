## compare_effeciency
- thresholdの値をfitted sigmaを用いて調節, eff-threshold依存性を描く

## compare_effeciency_by_predestal
- ADC value 900 - 1500 を1刻みで動かしながらeffeciencyを計算する
- effeciencyの計算方法
    - 対象となるchの鉛直方向で7個以上のchで(宇宙線fitの)MPVよりもADCが大きいchを計算の対象とした
    - 上記の条件のもとで対象となっているchが基準のADC value(900-1500)よりも大きいか小さいかでeffeciencyを見積もる
    - TrackSeekerクラスを継承して, TrackSeekerとは違うEffeciencyの計算方法を実装している
- Usage
    - ROOTのTGraphによってグラフが書き出される
    - 例えば, 3chのeffeciencyを計算したければ以下のように書く
        ```bash
        python3 compare_effeciency_by_pedestal 3
        ```
    - xargsで全チャンネルのグラフを作るなら以下
        ```bash
        seq 0 63 | xargs -I@ -P$(nproc) python3 compare_effeciency_by_pedestal @
        ```