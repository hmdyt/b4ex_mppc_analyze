## ADC_par_HV_list
- chごとの (ADC count) / (HV) が記載されている
- ch番号, (ADC count)/(HV) の順

## InputDAC_voltage_dependence
- InputDACの値 (256 ~ 511) とそれに対応するInputDAC voltage [V]の関係性 (直線) のパラメータが載っている
- ch番号, a, b の順
    ```
    (InputDAC voltage) = a * (InputDAC value) + b
    ```

## HV_ADC_pol1_list
- 宇宙線キャリブレーションの結果が書き込まれたファイル
- ch番号, a, b の順
    ```
    (ADC value) = a * (statusHV) + b
    ```

## fitMuonCalibration
- class MuonCalibrationといくつかのテスト用関数が入っている
### class MuonCalibration
- コンストラクタ
    - 測定時のHVと測定ファイルを教える
    - fit_rangeを呼び出してfittingに用いるパラメータを読み込む
- void set_ch(int)
    - ほとんどのメンバ関数は一つのchに対する操作となる
    - このメソッドでどのchへの操作にするか決める
- void fit()
    - 現在選択されているchに対して, fitを行う
- void save_as(TString)
    - 現在選択されているchのhistを任意の名前で保存する (png, svg, pdf, rootなど)

## make_hitmap_3D.py
- イベントディスプレイをpng, htmlで出力する
- 例えば, ADV_threshold = 1200, run999.rootの100event目をターゲットとするなら以下のように使う
```bash
python3 make_hitmap_3D.py 1200 100 "run999.root"
```