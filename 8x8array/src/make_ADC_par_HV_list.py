import pickle
from pyroot_easiroc import CalibrationData

cds: CalibrationData.CalibrationDatas = pickle.load(open("cds.pickle", 'rb'))

with open("ADC_par_HV_list", 'w') as f:
    for ch in range(64):
        s = "{} {}\n".format(ch, cds._HV_one_photon_TF1s[ch].GetParameter(0))
        f.write(s)
