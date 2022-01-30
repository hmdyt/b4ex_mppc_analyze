import sys

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


REFERENCE_CH = 0
REFERENCE_CH_DAC = 256 + 64

target_ADC = int(sys.argv[1])
target_HV = [ADC_to_HV(ch, target_ADC) for ch in range(64)]
statusHV = target_HV[REFERENCE_CH] + DAC_to_HV(REFERENCE_CH, REFERENCE_CH_DAC)
diff_HV = [target_HV[ch] - target_HV[REFERENCE_CH] for ch in range(64)]
diff_HV_DAC = [-diff_HV[ch] / InputDAC_voltage_dependence[ch][1] + REFERENCE_CH_DAC for ch in range(64)]

# debug output
for ch in range(64):
    ans = HV_to_ADC(ch, statusHV - DAC_to_HV(ch, int(diff_HV_DAC[ch])))
    print(ans)

for i in range(64):
    if diff_HV_DAC[i] < 256:
        diff_HV_DAC[i] = "256 # {}".format(diff_HV_DAC[i])
    elif 511 < diff_HV_DAC[i]:
        diff_HV_DAC[i] = "511 # {}".format(diff_HV_DAC[i])
    else:
        diff_HV_DAC[i] = str(int(diff_HV_DAC[i]))


with open("InputDAC.yml", 'w') as f:
    f.write("# reference channel {}\n".format(REFERENCE_CH))
    f.write("# targetADC = {}\n".format(target_ADC))
    f.write("# statusHV {}\n\n".format(statusHV))
    f.write("EASIROC1:\n")
    f.write("    Input 8-bit DAC:\n")
    for i in range(0, 32):
        f.write("    - {}\n".format(diff_HV_DAC[i]))
    f.write("EASIROC2:\n")
    f.write("    Input 8-bit DAC:\n")
    for i in range(32, 64):
        f.write("    - {}\n".format(diff_HV_DAC[i]))
