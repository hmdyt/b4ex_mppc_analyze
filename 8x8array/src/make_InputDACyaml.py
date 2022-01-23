import matplotlib.pyplot as plt
import numpy as np

with open("InputDAC_voltage_dependence") as f:
    InputDAC_voltage_dependence = f.read().split('\n')[0:-1]
    InputDAC_voltage_dependence = [list(map(float, v.split(" "))) for v in InputDAC_voltage_dependence]
with open("HV_ADC_pol1_list") as f:
    HV_ADC_pol1_list = f.read().split('\n')[1:-1]
    HV_ADC_pol1_list = [list(map(float, v.split(" ")[0:-1])) for v in HV_ADC_pol1_list]


def fetch_params(ch):
    _, a1, b1 = HV_ADC_pol1_list[ch]
    _, a2, b2 = InputDAC_voltage_dependence[ch]
    return a1, a2, b1, b2


def HV_to_ADC(ch, HV):
    a1, a2, b1, b2 = fetch_params(ch)
    return a1*HV + b1


def ADC_to_HV(ch, ADC):
    a1, a2, b1, b2 = fetch_params(ch)
    return (ADC - b1) / a1


def DAC_to_HV(ch, DAC):
    a1, a2, b1, b2 = fetch_params(ch)
    return a2*DAC + b2


def HV_to_DAC(ch, HV):
    a1, a2, b1, b2 = fetch_params(ch)
    return (HV - b2) / a2


target_ADC = 1600
target_HV = [ADC_to_HV(ch, target_ADC) for ch in range(64)]
statusHV = target_HV[33]
diff_HV = [target_HV[ch] - statusHV for ch in range(64)]
diff_HV_DAC = [HV_to_DAC(ch, diff_HV[ch]) for ch in range(64)]

with open("InputDAC.yml", 'w') as f:
    f.write("#statusHV {}\n".format(statusHV))
    f.write("EASIROC1:\n")
    f.write("    Input 8-bit DAC:\n")
    for i in range(0, 32):
        f.write("    - {}\n".format(int(diff_HV_DAC[i])))
    f.write("EASIROC2:\n")
    f.write("    Input 8-bit DAC:\n")
    for i in range(32, 64):
        f.write("    - {}\n".format(int(diff_HV_DAC[i])))
