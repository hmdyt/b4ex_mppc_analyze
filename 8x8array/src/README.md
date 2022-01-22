## ADC_par_HV_list
- chごとの (ADC count) / (HV) が記載されている
- ch番号, (ADC count)/(HV) の順

## InputDAC_voltage_dependence
- InputDACの値 (256 ~ 511) とそれに対応するInputDAC voltage [V]の関係性 (直線) のパラメータが載っている
- ch番号, a, b の順
    ```
    (InputDAC voltage) = a * (InputDAC value) + b
    ```