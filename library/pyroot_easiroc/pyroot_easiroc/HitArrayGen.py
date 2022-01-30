from tqdm import tqdm
import uproot
import numpy as np
import pickle
from . import calibrationUtils as util


class HitArrayGen:
    CHANNELS_UPSIDE = np.array([[i for i in range(0 + (4 * layer), 4 + (4 * layer))] for layer in range(8)])
    CHANNELS_DOWNSIDE = np.fliplr(np.array([[i for i in range(60 - (4 * layer), 64 - (4 * layer))] for layer in range(8)]))

    def __init__(self, rootfile_path):
        """
        NOT compatible Regular expression (ex. *, [0-9])
        """
        self._check_uproot_version()
        self._check_rootfile_extension(rootfile_path)
        self._load_rootfile(rootfile_path)
        print("{}\n {} event laoded.".format(self._rootfile_path, self._n_event))
        self._prepare_variables()

    def _check_uproot_version(self):
        if not int(uproot.__version__[0]) == 4:
            print("class HitArrayGen require uproot ver 4, current ver {}".format(uproot.__version__))
            exit()

    def _check_rootfile_extension(self, rootfile_path):
        if not rootfile_path[-5:] == ".root":
            print("rootfile_path must be finish '.root'")

    def _prepare_variables(self):
        self._thresholds = np.array([1200 for _ in range(64)])

    def _load_rootfile(self, rootfile_path):
        self._rootfile_path = rootfile_path
        with uproot.open(self._rootfile_path) as file:
            self._tree = file["tree"]
            self._VadcHigh = self._tree["VadcHigh"].array(library="np")
        self._n_event = len(self._VadcHigh)

    def set_threshold(self, ch, adc_th):
        self._thresholds[ch] = adc_th

    def generate_hit_array(self):
        # ch order => upside, downside order
        Vadc_upside = self._VadcHigh[:, self.CHANNELS_UPSIDE]
        Vadc_downside = self._VadcHigh[:, self.CHANNELS_DOWNSIDE]
        # in order to make crossed map, duplicate vector
        self._Vadc_upside_map = np.tile(Vadc_upside, (1, 1, 4)).reshape(self._n_event, 8, 4, 4).transpose(0, 1, 3, 2)
        self._Vadc_downside_map = np.tile(Vadc_downside, (1, 1, 4)).reshape(self._n_event, 8, 4, 4)
        # ch order => upside, downside order too (threshold)
        self._thresholds_upside_map = np.tile(self._thresholds[self.CHANNELS_UPSIDE], (1, 4)).reshape(8, 4, 4).transpose(0, 2, 1)
        self._thresholds_downside_map = np.tile(self._thresholds[self.CHANNELS_DOWNSIDE], (1, 4)).reshape(8, 4, 4)
        # make crossed map
        self._hit_array = (self._thresholds_upside_map < self._Vadc_upside_map) * (self._thresholds_downside_map < self._Vadc_downside_map)

    def get_hit_array(self):
        return self._hit_array
