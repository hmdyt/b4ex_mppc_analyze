import pickle
from pyroot_easiroc import CalibrationData

cds: CalibrationData.CalibrationDatas = pickle.load(open("cds.pickle", 'rb'))
cds.make_yml_InputDAC(70)
