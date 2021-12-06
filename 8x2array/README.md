## How to tune parameters
- jsonファイルにパラメータをいい感じに書く ([例: json](/8x2array/json/cal_20211206_15_ch4.json))
- jsonファイルのパスを`getCalibrationParams()`に渡す
    - こんな感じで書いて => [run_calibration.py](/8x2array/src/run_calibration.py)
    - こんな感じで実行
    ```bash
    [host@user b4ex_mppc_analyze]$ python3 8x2array/src/run_calibration.py 
    ```
    - ROOTの窓が欲しいなら[run_calibration.py](/8x2array/src/run_calibration.py)内の`r.gROOT.SetBatch()`を消して、
    ```bash
    [host@user b4ex_mppc_analyze]$ python3 -i 8x2array/src/run_calibration.py 
    ```
    - 必ずリポジトリの一番上から実行すること
- fitされた画像がjsonファイルに指定した場所に保存されているので確認
    - あかんかったらパラメータを修正

### 例
- [これ](/8x2array/json/cal_20211206_14_ch8.json)がこう

    ![ex](/docs/images/example_fitted.png)