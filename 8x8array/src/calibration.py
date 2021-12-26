from pyroot_easiroc import CalibrationData
import ROOT as r
r.gROOT.SetBatch()

cds = CalibrationData.CalibrationDatas()

# setHV 52.4
cds.set_calb_data("./img_529", "52.9")

cds.get_calb_data("52.9").set_hist(0, "/data/hamada/easiroc_data/cal_20211226_03.root", 4)
cds.get_calb_data("52.9").set_hist(1, "/data/hamada/easiroc_data/cal_20211226_03.root", 5)
cds.get_calb_data("52.9").set_hist(2, "/data/hamada/easiroc_data/cal_20211226_03.root", 6)
cds.get_calb_data("52.9").set_hist(3, "/data/hamada/easiroc_data/cal_20211226_03.root", 7)
cds.get_calb_data("52.9").set_hist(4, "/data/hamada/easiroc_data/cal_20211226_03.root", 8)
cds.get_calb_data("52.9").set_hist(5, "/data/hamada/easiroc_data/cal_20211226_03.root", 9)
cds.get_calb_data("52.9").set_hist(6, "/data/hamada/easiroc_data/cal_20211226_03.root", 10)
cds.get_calb_data("52.9").set_hist(7, "/data/hamada/easiroc_data/cal_20211226_03.root", 11)

cds.get_calb_data("52.9").set_hist(8, "/data/hamada/easiroc_data/cal_20211226_06.root", 4)
cds.get_calb_data("52.9").set_hist(9, "/data/hamada/easiroc_data/cal_20211226_06.root", 5)
cds.get_calb_data("52.9").set_hist(10, "/data/hamada/easiroc_data/cal_20211226_06.root", 6)
cds.get_calb_data("52.9").set_hist(11, "/data/hamada/easiroc_data/cal_20211226_06.root", 7)
cds.get_calb_data("52.9").set_hist(12, "/data/hamada/easiroc_data/cal_20211226_06.root", 8)
cds.get_calb_data("52.9").set_hist(13, "/data/hamada/easiroc_data/cal_20211226_06.root", 9)
cds.get_calb_data("52.9").set_hist(14, "/data/hamada/easiroc_data/cal_20211226_06.root", 10)
cds.get_calb_data("52.9").set_hist(15, "/data/hamada/easiroc_data/cal_20211226_06.root", 11)

cds.get_calb_data("52.9").set_hist(16, "/data/hamada/easiroc_data/cal_20211226_09.root", 4)
cds.get_calb_data("52.9").set_hist(17, "/data/hamada/easiroc_data/cal_20211226_09.root", 5)
cds.get_calb_data("52.9").set_hist(18, "/data/hamada/easiroc_data/cal_20211226_09.root", 6)
cds.get_calb_data("52.9").set_hist(19, "/data/hamada/easiroc_data/cal_20211226_09.root", 7)
cds.get_calb_data("52.9").set_hist(20, "/data/hamada/easiroc_data/cal_20211226_09.root", 8)
cds.get_calb_data("52.9").set_hist(21, "/data/hamada/easiroc_data/cal_20211226_09.root", 9)
cds.get_calb_data("52.9").set_hist(22, "/data/hamada/easiroc_data/cal_20211226_09.root", 10)
cds.get_calb_data("52.9").set_hist(23, "/data/hamada/easiroc_data/cal_20211226_09.root", 11)

cds.get_calb_data("52.9").set_hist(24, "/data/hamada/easiroc_data/cal_20211226_12.root", 4)
cds.get_calb_data("52.9").set_hist(25, "/data/hamada/easiroc_data/cal_20211226_12.root", 5)
cds.get_calb_data("52.9").set_hist(26, "/data/hamada/easiroc_data/cal_20211226_12.root", 6)
cds.get_calb_data("52.9").set_hist(27, "/data/hamada/easiroc_data/cal_20211226_12.root", 7)
cds.get_calb_data("52.9").set_hist(28, "/data/hamada/easiroc_data/cal_20211226_12.root", 8)
cds.get_calb_data("52.9").set_hist(29, "/data/hamada/easiroc_data/cal_20211226_12.root", 9)
cds.get_calb_data("52.9").set_hist(30, "/data/hamada/easiroc_data/cal_20211226_12.root", 10)
cds.get_calb_data("52.9").set_hist(31, "/data/hamada/easiroc_data/cal_20211226_12.root", 11)

cds.get_calb_data("52.9").set_hist(32, "/data/hamada/easiroc_data/cal_20211226_15.root", 4)
cds.get_calb_data("52.9").set_hist(33, "/data/hamada/easiroc_data/cal_20211226_15.root", 5)
cds.get_calb_data("52.9").set_hist(34, "/data/hamada/easiroc_data/cal_20211226_15.root", 6)
cds.get_calb_data("52.9").set_hist(35, "/data/hamada/easiroc_data/cal_20211226_15.root", 7)
cds.get_calb_data("52.9").set_hist(36, "/data/hamada/easiroc_data/cal_20211226_15.root", 8)
cds.get_calb_data("52.9").set_hist(37, "/data/hamada/easiroc_data/cal_20211226_15.root", 9)
cds.get_calb_data("52.9").set_hist(38, "/data/hamada/easiroc_data/cal_20211226_15.root", 10)
cds.get_calb_data("52.9").set_hist(39, "/data/hamada/easiroc_data/cal_20211226_15.root", 11)

cds.get_calb_data("52.9").set_hist(40, "/data/hamada/easiroc_data/cal_20211226_18.root", 4)
cds.get_calb_data("52.9").set_hist(41, "/data/hamada/easiroc_data/cal_20211226_18.root", 5)
cds.get_calb_data("52.9").set_hist(42, "/data/hamada/easiroc_data/cal_20211226_18.root", 6)
cds.get_calb_data("52.9").set_hist(43, "/data/hamada/easiroc_data/cal_20211226_18.root", 7)
cds.get_calb_data("52.9").set_hist(44, "/data/hamada/easiroc_data/cal_20211226_18.root", 8)
cds.get_calb_data("52.9").set_hist(45, "/data/hamada/easiroc_data/cal_20211226_18.root", 9)
cds.get_calb_data("52.9").set_hist(46, "/data/hamada/easiroc_data/cal_20211226_18.root", 10)
cds.get_calb_data("52.9").set_hist(47, "/data/hamada/easiroc_data/cal_20211226_18.root", 11)

cds.get_calb_data("52.9").set_hist(48, "/data/hamada/easiroc_data/cal_20211226_21.root", 4)
cds.get_calb_data("52.9").set_hist(49, "/data/hamada/easiroc_data/cal_20211226_21.root", 5)
cds.get_calb_data("52.9").set_hist(50, "/data/hamada/easiroc_data/cal_20211226_21.root", 6)
cds.get_calb_data("52.9").set_hist(51, "/data/hamada/easiroc_data/cal_20211226_21.root", 7)
cds.get_calb_data("52.9").set_hist(52, "/data/hamada/easiroc_data/cal_20211226_21.root", 8)
cds.get_calb_data("52.9").set_hist(53, "/data/hamada/easiroc_data/cal_20211226_21.root", 9)
cds.get_calb_data("52.9").set_hist(54, "/data/hamada/easiroc_data/cal_20211226_21.root", 10)
cds.get_calb_data("52.9").set_hist(55, "/data/hamada/easiroc_data/cal_20211226_21.root", 11)

cds.get_calb_data("52.9").set_hist(56, "/data/hamada/easiroc_data/cal_20211226_24.root", 4)
cds.get_calb_data("52.9").set_hist(57, "/data/hamada/easiroc_data/cal_20211226_24.root", 5)
cds.get_calb_data("52.9").set_hist(58, "/data/hamada/easiroc_data/cal_20211226_24.root", 6)
cds.get_calb_data("52.9").set_hist(59, "/data/hamada/easiroc_data/cal_20211226_24.root", 7)
cds.get_calb_data("52.9").set_hist(60, "/data/hamada/easiroc_data/cal_20211226_24.root", 8)
cds.get_calb_data("52.9").set_hist(61, "/data/hamada/easiroc_data/cal_20211226_24.root", 9)
cds.get_calb_data("52.9").set_hist(62, "/data/hamada/easiroc_data/cal_20211226_24.root", 10)
cds.get_calb_data("52.9").set_hist(63, "/data/hamada/easiroc_data/cal_20211226_24.root", 11)

cds.get_calb_data("52.9").fit_multi_gaus(
    0,
    peak_search_range=(0, 1500),
    fitting_range=(780, 1050),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    1,
    peak_search_range=(0, 1500),
    fitting_range=(780, 1000),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    2,
    peak_search_range=(0, 1500),
    fitting_range=(780, 1250),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    3,
    peak_search_range=(0, 2000),
    fitting_range=(900, 1650),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    4,
    peak_search_range=(0, 2000),
    fitting_range=(980, 1800),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    5,
    peak_search_range=(0, 2000),
    fitting_range=(1020, 1930),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    6,
    peak_search_range=(0, 2500),
    fitting_range=(1150, 2000),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    7,
    peak_search_range=(0, 2500),
    fitting_range=(1150, 2200),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    8,
    peak_search_range=(0, 2500),
    fitting_range=(760, 990),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    9,
    peak_search_range=(0, 2500),
    fitting_range=(800, 970),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    10,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1180),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    11,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1300),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    12,
    peak_search_range=(0, 2500),
    fitting_range=(850, 1500),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    13,
    peak_search_range=(0, 2500),
    fitting_range=(850, 1500),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    14,
    peak_search_range=(0, 2500),
    fitting_range=(900, 1700),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    15,
    peak_search_range=(0, 2500),
    fitting_range=(1000, 1900),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    16,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1000),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    17,
    peak_search_range=(0, 2500),
    fitting_range=(800, 970),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    18,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1130),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    19,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1230),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    20,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1450),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    21,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1500),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    22,
    peak_search_range=(0, 2500),
    fitting_range=(850, 1550),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    23,
    peak_search_range=(0, 2500),
    fitting_range=(850, 1600),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    24,
    peak_search_range=(0, 2500),
    fitting_range=(800, 980),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    25,
    peak_search_range=(0, 2500),
    fitting_range=(800, 910),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    26,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1060),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    27,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1280),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    28,
    peak_search_range=(0, 2500),
    fitting_range=(850, 1550),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    29,
    peak_search_range=(0, 2500),
    fitting_range=(850, 1570),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    30,
    peak_search_range=(0, 2500),
    fitting_range=(850, 1480),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    31,
    peak_search_range=(0, 2500),
    fitting_range=(800,1170),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    32,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1000),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    33,
    peak_search_range=(0, 2500),
    fitting_range=(790, 1030),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    34,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1250),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    35,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1450),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    36,
    peak_search_range=(0, 2500),
    fitting_range=(900, 1700),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    37,
    peak_search_range=(0, 2500),
    fitting_range=(900, 1850),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    38,
    peak_search_range=(0, 2500),
    fitting_range=(1050, 2020),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    39,
    peak_search_range=(0, 2500),
    fitting_range=(930, 1700),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    40,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1050),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    41,
    peak_search_range=(0, 2500),
    fitting_range=(800, 970),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    42,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1350),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    43,
    peak_search_range=(0, 2500),
    fitting_range=(850, 1380),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    44,
    peak_search_range=(0, 2500),
    fitting_range=(900, 1650),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    45,
    peak_search_range=(0, 2500),
    fitting_range=(900, 1650),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    46,
    peak_search_range=(0, 2500),
    fitting_range=(790, 1150),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    47,
    peak_search_range=(0, 2500),
    fitting_range=(1100, 2050),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    48,
    peak_search_range=(0, 2500),
    fitting_range=(780, 1030),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    49,
    peak_search_range=(0, 2500),
    fitting_range=(780, 1030),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    50,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1250),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    51,
    peak_search_range=(0, 2500),
    fitting_range=(850, 1500),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    52,
    peak_search_range=(0, 2500),
    fitting_range=(900, 1700),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    53,
    peak_search_range=(0, 2500),
    fitting_range=(950, 1730),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    54,
    peak_search_range=(0, 2500),
    fitting_range=(1100, 2180),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    55,
    peak_search_range=(0, 2500),
    fitting_range=(1170, 2150),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    56,
    peak_search_range=(0, 2500),
    fitting_range=(800, 930),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    57,
    peak_search_range=(0, 2500),
    fitting_range=(800, 910),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    58,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1030),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    59,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1120),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    60,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1320),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    61,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1350),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    62,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1450),
    peak_search_sigma=10
)
cds.get_calb_data("52.9").fit_multi_gaus(
    63,
    peak_search_range=(0, 2500),
    fitting_range=(800, 1500),
    peak_search_sigma=10
)

# setHV 52.6
cds.set_calb_data("./img_531", "53.1")

cds.get_calb_data("53.1").set_hist(0, "/data/hamada/easiroc_data/cal_20211226_04.root", 4)
cds.get_calb_data("53.1").set_hist(1, "/data/hamada/easiroc_data/cal_20211226_04.root", 5)
cds.get_calb_data("53.1").set_hist(2, "/data/hamada/easiroc_data/cal_20211226_04.root", 6)
cds.get_calb_data("53.1").set_hist(3, "/data/hamada/easiroc_data/cal_20211226_04.root", 7)
cds.get_calb_data("53.1").set_hist(4, "/data/hamada/easiroc_data/cal_20211226_04.root", 8)
cds.get_calb_data("53.1").set_hist(5, "/data/hamada/easiroc_data/cal_20211226_04.root", 9)
cds.get_calb_data("53.1").set_hist(6, "/data/hamada/easiroc_data/cal_20211226_04.root", 10)
cds.get_calb_data("53.1").set_hist(7, "/data/hamada/easiroc_data/cal_20211226_04.root", 11)

cds.get_calb_data("53.1").set_hist(8, "/data/hamada/easiroc_data/cal_20211226_07.root", 4)
cds.get_calb_data("53.1").set_hist(9, "/data/hamada/easiroc_data/cal_20211226_07.root", 5)
cds.get_calb_data("53.1").set_hist(10, "/data/hamada/easiroc_data/cal_20211226_07.root", 6)
cds.get_calb_data("53.1").set_hist(11, "/data/hamada/easiroc_data/cal_20211226_07.root", 7)
cds.get_calb_data("53.1").set_hist(12, "/data/hamada/easiroc_data/cal_20211226_07.root", 8)
cds.get_calb_data("53.1").set_hist(13, "/data/hamada/easiroc_data/cal_20211226_07.root", 9)
cds.get_calb_data("53.1").set_hist(14, "/data/hamada/easiroc_data/cal_20211226_07.root", 10)
cds.get_calb_data("53.1").set_hist(15, "/data/hamada/easiroc_data/cal_20211226_07.root", 11)

cds.get_calb_data("53.1").set_hist(16, "/data/hamada/easiroc_data/cal_20211226_10.root", 4)
cds.get_calb_data("53.1").set_hist(17, "/data/hamada/easiroc_data/cal_20211226_10.root", 5)
cds.get_calb_data("53.1").set_hist(18, "/data/hamada/easiroc_data/cal_20211226_10.root", 6)
cds.get_calb_data("53.1").set_hist(19, "/data/hamada/easiroc_data/cal_20211226_10.root", 7)
cds.get_calb_data("53.1").set_hist(20, "/data/hamada/easiroc_data/cal_20211226_10.root", 8)
cds.get_calb_data("53.1").set_hist(21, "/data/hamada/easiroc_data/cal_20211226_10.root", 9)
cds.get_calb_data("53.1").set_hist(22, "/data/hamada/easiroc_data/cal_20211226_10.root", 10)
cds.get_calb_data("53.1").set_hist(23, "/data/hamada/easiroc_data/cal_20211226_10.root", 11)

cds.get_calb_data("53.1").set_hist(24, "/data/hamada/easiroc_data/cal_20211226_13.root", 4)
cds.get_calb_data("53.1").set_hist(25, "/data/hamada/easiroc_data/cal_20211226_13.root", 5)
cds.get_calb_data("53.1").set_hist(26, "/data/hamada/easiroc_data/cal_20211226_13.root", 6)
cds.get_calb_data("53.1").set_hist(27, "/data/hamada/easiroc_data/cal_20211226_13.root", 7)
cds.get_calb_data("53.1").set_hist(28, "/data/hamada/easiroc_data/cal_20211226_13.root", 8)
cds.get_calb_data("53.1").set_hist(29, "/data/hamada/easiroc_data/cal_20211226_13.root", 9)
cds.get_calb_data("53.1").set_hist(30, "/data/hamada/easiroc_data/cal_20211226_13.root", 10)
cds.get_calb_data("53.1").set_hist(31, "/data/hamada/easiroc_data/cal_20211226_13.root", 11)

cds.get_calb_data("53.1").set_hist(32, "/data/hamada/easiroc_data/cal_20211226_16.root", 4)
cds.get_calb_data("53.1").set_hist(33, "/data/hamada/easiroc_data/cal_20211226_16.root", 5)
cds.get_calb_data("53.1").set_hist(34, "/data/hamada/easiroc_data/cal_20211226_16.root", 6)
cds.get_calb_data("53.1").set_hist(35, "/data/hamada/easiroc_data/cal_20211226_16.root", 7)
cds.get_calb_data("53.1").set_hist(36, "/data/hamada/easiroc_data/cal_20211226_16.root", 8)
cds.get_calb_data("53.1").set_hist(37, "/data/hamada/easiroc_data/cal_20211226_16.root", 9)
cds.get_calb_data("53.1").set_hist(38, "/data/hamada/easiroc_data/cal_20211226_16.root", 10)
cds.get_calb_data("53.1").set_hist(39, "/data/hamada/easiroc_data/cal_20211226_16.root", 11)

cds.get_calb_data("53.1").set_hist(40, "/data/hamada/easiroc_data/cal_20211226_19.root", 4)
cds.get_calb_data("53.1").set_hist(41, "/data/hamada/easiroc_data/cal_20211226_19.root", 5)
cds.get_calb_data("53.1").set_hist(42, "/data/hamada/easiroc_data/cal_20211226_19.root", 6)
cds.get_calb_data("53.1").set_hist(43, "/data/hamada/easiroc_data/cal_20211226_19.root", 7)
cds.get_calb_data("53.1").set_hist(44, "/data/hamada/easiroc_data/cal_20211226_19.root", 8)
cds.get_calb_data("53.1").set_hist(45, "/data/hamada/easiroc_data/cal_20211226_19.root", 9)
cds.get_calb_data("53.1").set_hist(46, "/data/hamada/easiroc_data/cal_20211226_19.root", 10)
cds.get_calb_data("53.1").set_hist(47, "/data/hamada/easiroc_data/cal_20211226_19.root", 11)

cds.get_calb_data("53.1").set_hist(48, "/data/hamada/easiroc_data/cal_20211226_22.root", 4)
cds.get_calb_data("53.1").set_hist(49, "/data/hamada/easiroc_data/cal_20211226_22.root", 5)
cds.get_calb_data("53.1").set_hist(50, "/data/hamada/easiroc_data/cal_20211226_22.root", 6)
cds.get_calb_data("53.1").set_hist(51, "/data/hamada/easiroc_data/cal_20211226_22.root", 7)
cds.get_calb_data("53.1").set_hist(52, "/data/hamada/easiroc_data/cal_20211226_22.root", 8)
cds.get_calb_data("53.1").set_hist(53, "/data/hamada/easiroc_data/cal_20211226_22.root", 9)
cds.get_calb_data("53.1").set_hist(54, "/data/hamada/easiroc_data/cal_20211226_22.root", 10)
cds.get_calb_data("53.1").set_hist(55, "/data/hamada/easiroc_data/cal_20211226_22.root", 11)

cds.get_calb_data("53.1").set_hist(56, "/data/hamada/easiroc_data/cal_20211226_25.root", 4)
cds.get_calb_data("53.1").set_hist(57, "/data/hamada/easiroc_data/cal_20211226_25.root", 5)
cds.get_calb_data("53.1").set_hist(58, "/data/hamada/easiroc_data/cal_20211226_25.root", 6)
cds.get_calb_data("53.1").set_hist(59, "/data/hamada/easiroc_data/cal_20211226_25.root", 7)
cds.get_calb_data("53.1").set_hist(60, "/data/hamada/easiroc_data/cal_20211226_25.root", 8)
cds.get_calb_data("53.1").set_hist(61, "/data/hamada/easiroc_data/cal_20211226_25.root", 9)
cds.get_calb_data("53.1").set_hist(62, "/data/hamada/easiroc_data/cal_20211226_25.root", 10)
cds.get_calb_data("53.1").set_hist(63, "/data/hamada/easiroc_data/cal_20211226_25.root", 11)

cds.get_calb_data("53.1").fit_multi_gaus(
    ch=0,
    peak_search_range=(0, 4096),
    fitting_range=(780, 1030),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=1,
    peak_search_range=(0, 4096),
    fitting_range=(780, 1030),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=2,
    peak_search_range=(0, 4096),
    fitting_range=(780, 1350),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=3,
    peak_search_range=(0, 4096),
    fitting_range=(920, 1750),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=4,
    peak_search_range=(0, 4096),
    fitting_range=(1000, 1960),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=5,
    peak_search_range=(0, 4096),
    fitting_range=(1050, 2050),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=6,
    peak_search_range=(0, 4096),
    fitting_range=(1190, 2235),
    peak_search_sigma=10
)

cds.get_calb_data("53.1").fit_multi_gaus(
    ch=7,
    peak_search_range=(0, 4096),
    fitting_range=(1260, 2350),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=8,
    peak_search_range=(0, 4096),
    fitting_range=(810, 990),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=9,
    peak_search_range=(0, 4096),
    fitting_range=(810, 970),
    peak_search_sigma=10
)

cds.get_calb_data("53.1").fit_multi_gaus(
    ch=10,
    peak_search_range=(0, 4096),
    fitting_range=(810, 1170),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=11,
    peak_search_range=(0, 4096),
    fitting_range=(810, 1390),
    peak_search_sigma=10
)

cds.get_calb_data("53.1").fit_multi_gaus(
    ch=12,
    peak_search_range=(0, 4096),
    fitting_range=(880, 1630),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=13,
    peak_search_range=(0, 4096),
    fitting_range=(930, 1680),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=14,
    peak_search_range=(0, 4096),
    fitting_range=(930, 1770),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=15,
    peak_search_range=(0, 4096),
    fitting_range=(1020, 2050),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=16,
    peak_search_range=(0, 4096),
    fitting_range=(800, 950),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=17,
    peak_search_range=(0, 4096),
    fitting_range=(800, 950),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=18,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1000),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=19,
    peak_search_range=(0, 4096),
    fitting_range=(810, 1040),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=20,
    peak_search_range=(0, 4096),
    fitting_range=(820, 1170),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=21,
    peak_search_range=(0, 4096),
    fitting_range=(820, 1170),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=22,
    peak_search_range=(0, 4096),
    fitting_range=(820, 1170),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=23,
    peak_search_range=(0, 4096),
    fitting_range=(820, 1170),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=24,
    peak_search_range=(0, 4096),
    fitting_range=(800, 990),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=25,
    peak_search_range=(0, 4096),
    fitting_range=(800, 910),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=26,
    peak_search_range=(0, 4096),
    fitting_range=(810, 1120),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=27,
    peak_search_range=(0, 4096),
    fitting_range=(810, 1320),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=28,
    peak_search_range=(0, 4096),
    fitting_range=(880, 1760),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=29,
    peak_search_range=(0, 4096),
    fitting_range=(880, 1700),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=30,
    peak_search_range=(0, 4096),
    fitting_range=(880, 1600),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=31,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1300),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=32,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1070),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=33,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1030),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=34,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1350),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=35,
    peak_search_range=(0, 4096),
    fitting_range=(870, 1560),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=36,
    peak_search_range=(0, 4096),
    fitting_range=(950, 1900),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=37,
    peak_search_range=(0, 4096),
    fitting_range=(1000, 2070),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=38,
    peak_search_range=(0, 4096),
    fitting_range=(1160, 2280),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=39,
    peak_search_range=(0, 4096),
    fitting_range=(1040, 1920),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=40,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1050),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=41,
    peak_search_range=(0, 4096),
    fitting_range=(800, 980),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=42,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1370),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=43,
    peak_search_range=(0, 4096),
    fitting_range=(870, 1450),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=44,
    peak_search_range=(0, 4096),
    fitting_range=(930, 1720),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=45,
    peak_search_range=(0, 4096),
    fitting_range=(940, 1780),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=46,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1170),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=47,
    peak_search_range=(0, 4096),
    fitting_range=(1200, 2300),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=48,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1030),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=49,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1030),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=50,
    peak_search_range=(0, 4096),
    fitting_range=(800, 1250),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=51,
    peak_search_range=(0, 4096),
    fitting_range=(875, 1600),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=52,
    peak_search_range=(0, 4096),
    fitting_range=(930, 1820),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=53,
    peak_search_range=(0, 4096),
    fitting_range=(990, 1900),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=54,
    peak_search_range=(0, 4096),
    fitting_range=(1200, 2300),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=55,
    peak_search_range=(0, 2400),
    fitting_range=(1200, 2350),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=56,
    peak_search_range=(0, 2400),
    fitting_range=(800, 930),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=57,
    peak_search_range=(0, 2400),
    fitting_range=(800, 930),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=58,
    peak_search_range=(0, 2400),
    fitting_range=(800, 980),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=59,
    peak_search_range=(0, 2400),
    fitting_range=(800, 1020),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=60,
    peak_search_range=(0, 2400),
    fitting_range=(800, 1140),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=61,
    peak_search_range=(0, 2400),
    fitting_range=(800, 1190),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=62,
    peak_search_range=(0, 2400),
    fitting_range=(800, 1220),
    peak_search_sigma=10
)
cds.get_calb_data("53.1").fit_multi_gaus(
    ch=63,
    peak_search_range=(0, 2400),
    fitting_range=(800, 1300),
    peak_search_sigma=10
)

# setHV 52.8
cds.set_calb_data("./img_533", "53.3")

cds.get_calb_data("53.3").set_hist(0, "/data/hamada/easiroc_data/cal_20211226_05.root", 4)
cds.get_calb_data("53.3").set_hist(1, "/data/hamada/easiroc_data/cal_20211226_05.root", 5)
cds.get_calb_data("53.3").set_hist(2, "/data/hamada/easiroc_data/cal_20211226_05.root", 6)
cds.get_calb_data("53.3").set_hist(3, "/data/hamada/easiroc_data/cal_20211226_05.root", 7)
cds.get_calb_data("53.3").set_hist(4, "/data/hamada/easiroc_data/cal_20211226_05.root", 8)
cds.get_calb_data("53.3").set_hist(5, "/data/hamada/easiroc_data/cal_20211226_05.root", 9)
cds.get_calb_data("53.3").set_hist(6, "/data/hamada/easiroc_data/cal_20211226_05.root", 10)
cds.get_calb_data("53.3").set_hist(7, "/data/hamada/easiroc_data/cal_20211226_05.root", 11)

cds.get_calb_data("53.3").set_hist(8, "/data/hamada/easiroc_data/cal_20211226_08.root", 4)
cds.get_calb_data("53.3").set_hist(9, "/data/hamada/easiroc_data/cal_20211226_08.root", 5)
cds.get_calb_data("53.3").set_hist(10, "/data/hamada/easiroc_data/cal_20211226_08.root", 6)
cds.get_calb_data("53.3").set_hist(11, "/data/hamada/easiroc_data/cal_20211226_08.root", 7)
cds.get_calb_data("53.3").set_hist(12, "/data/hamada/easiroc_data/cal_20211226_08.root", 8)
cds.get_calb_data("53.3").set_hist(13, "/data/hamada/easiroc_data/cal_20211226_08.root", 9)
cds.get_calb_data("53.3").set_hist(14, "/data/hamada/easiroc_data/cal_20211226_08.root", 10)
cds.get_calb_data("53.3").set_hist(15, "/data/hamada/easiroc_data/cal_20211226_08.root", 11)

cds.get_calb_data("53.3").set_hist(16, "/data/hamada/easiroc_data/cal_20211226_11.root", 4)
cds.get_calb_data("53.3").set_hist(17, "/data/hamada/easiroc_data/cal_20211226_11.root", 5)
cds.get_calb_data("53.3").set_hist(18, "/data/hamada/easiroc_data/cal_20211226_11.root", 6)
cds.get_calb_data("53.3").set_hist(19, "/data/hamada/easiroc_data/cal_20211226_11.root", 7)
cds.get_calb_data("53.3").set_hist(20, "/data/hamada/easiroc_data/cal_20211226_11.root", 8)
cds.get_calb_data("53.3").set_hist(21, "/data/hamada/easiroc_data/cal_20211226_11.root", 9)
cds.get_calb_data("53.3").set_hist(22, "/data/hamada/easiroc_data/cal_20211226_11.root", 10)
cds.get_calb_data("53.3").set_hist(23, "/data/hamada/easiroc_data/cal_20211226_11.root", 11)

cds.get_calb_data("53.3").set_hist(24, "/data/hamada/easiroc_data/cal_20211226_14.root", 4)
cds.get_calb_data("53.3").set_hist(25, "/data/hamada/easiroc_data/cal_20211226_14.root", 5)
cds.get_calb_data("53.3").set_hist(26, "/data/hamada/easiroc_data/cal_20211226_14.root", 6)
cds.get_calb_data("53.3").set_hist(27, "/data/hamada/easiroc_data/cal_20211226_14.root", 7)
cds.get_calb_data("53.3").set_hist(28, "/data/hamada/easiroc_data/cal_20211226_14.root", 8)
cds.get_calb_data("53.3").set_hist(29, "/data/hamada/easiroc_data/cal_20211226_14.root", 9)
cds.get_calb_data("53.3").set_hist(30, "/data/hamada/easiroc_data/cal_20211226_14.root", 10)
cds.get_calb_data("53.3").set_hist(31, "/data/hamada/easiroc_data/cal_20211226_14.root", 11)

cds.get_calb_data("53.3").set_hist(32, "/data/hamada/easiroc_data/cal_20211226_17.root", 4)
cds.get_calb_data("53.3").set_hist(33, "/data/hamada/easiroc_data/cal_20211226_17.root", 5)
cds.get_calb_data("53.3").set_hist(34, "/data/hamada/easiroc_data/cal_20211226_17.root", 6)
cds.get_calb_data("53.3").set_hist(35, "/data/hamada/easiroc_data/cal_20211226_17.root", 7)
cds.get_calb_data("53.3").set_hist(36, "/data/hamada/easiroc_data/cal_20211226_17.root", 8)
cds.get_calb_data("53.3").set_hist(37, "/data/hamada/easiroc_data/cal_20211226_17.root", 9)
cds.get_calb_data("53.3").set_hist(38, "/data/hamada/easiroc_data/cal_20211226_17.root", 10)
cds.get_calb_data("53.3").set_hist(39, "/data/hamada/easiroc_data/cal_20211226_17.root", 11)

cds.get_calb_data("53.3").set_hist(40, "/data/hamada/easiroc_data/cal_20211226_20.root", 4)
cds.get_calb_data("53.3").set_hist(41, "/data/hamada/easiroc_data/cal_20211226_20.root", 5)
cds.get_calb_data("53.3").set_hist(42, "/data/hamada/easiroc_data/cal_20211226_20.root", 6)
cds.get_calb_data("53.3").set_hist(43, "/data/hamada/easiroc_data/cal_20211226_20.root", 7)
cds.get_calb_data("53.3").set_hist(44, "/data/hamada/easiroc_data/cal_20211226_20.root", 8)
cds.get_calb_data("53.3").set_hist(45, "/data/hamada/easiroc_data/cal_20211226_20.root", 9)
cds.get_calb_data("53.3").set_hist(46, "/data/hamada/easiroc_data/cal_20211226_20.root", 10)
cds.get_calb_data("53.3").set_hist(47, "/data/hamada/easiroc_data/cal_20211226_20.root", 11)

cds.get_calb_data("53.3").set_hist(48, "/data/hamada/easiroc_data/cal_20211226_23.root", 4)
cds.get_calb_data("53.3").set_hist(49, "/data/hamada/easiroc_data/cal_20211226_23.root", 5)
cds.get_calb_data("53.3").set_hist(50, "/data/hamada/easiroc_data/cal_20211226_23.root", 6)
cds.get_calb_data("53.3").set_hist(51, "/data/hamada/easiroc_data/cal_20211226_23.root", 7)
cds.get_calb_data("53.3").set_hist(52, "/data/hamada/easiroc_data/cal_20211226_23.root", 8)
cds.get_calb_data("53.3").set_hist(53, "/data/hamada/easiroc_data/cal_20211226_23.root", 9)
cds.get_calb_data("53.3").set_hist(54, "/data/hamada/easiroc_data/cal_20211226_23.root", 10)
cds.get_calb_data("53.3").set_hist(55, "/data/hamada/easiroc_data/cal_20211226_23.root", 11)

cds.get_calb_data("53.3").set_hist(56, "/data/hamada/easiroc_data/cal_20211226_26.root", 4)
cds.get_calb_data("53.3").set_hist(57, "/data/hamada/easiroc_data/cal_20211226_26.root", 5)
cds.get_calb_data("53.3").set_hist(58, "/data/hamada/easiroc_data/cal_20211226_26.root", 6)
cds.get_calb_data("53.3").set_hist(59, "/data/hamada/easiroc_data/cal_20211226_26.root", 7)
cds.get_calb_data("53.3").set_hist(60, "/data/hamada/easiroc_data/cal_20211226_26.root", 8)
cds.get_calb_data("53.3").set_hist(61, "/data/hamada/easiroc_data/cal_20211226_26.root", 9)
cds.get_calb_data("53.3").set_hist(62, "/data/hamada/easiroc_data/cal_20211226_26.root", 10)
cds.get_calb_data("53.3").set_hist(63, "/data/hamada/easiroc_data/cal_20211226_26.root", 11)

cds.get_calb_data("53.3").fit_multi_gaus(
    0,
    peak_search_range=(0, 1500),
    fitting_range=(760, 1070),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    1,
    peak_search_range=(0, 2500),
    fitting_range=(780, 1080),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    2,
    peak_search_range=(0, 2500),
    fitting_range=(780, 1400),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    3,
    peak_search_range=(0, 2500),
    fitting_range=(900, 1850),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    4,
    peak_search_range=(0, 2500),
    fitting_range=(1050, 2150),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    5,
    peak_search_range=(0, 2500),
    fitting_range=(1150, 2220),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    6,
    peak_search_range=(0, 2500),
    fitting_range=(1200, 2380),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    7,
    peak_search_range=(0, 2700),
    fitting_range=(1350, 2480),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    8,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1020),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    9,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1050),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    10,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1250),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    11,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1450),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    12,
    peak_search_range=(0, 2700),
    fitting_range=(870, 1780),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    13,
    peak_search_range=(0, 2700),
    fitting_range=(900, 1800),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    14,
    peak_search_range=(0, 2700),
    fitting_range=(990, 1950),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    15,
    peak_search_range=(0, 2700),
    fitting_range=(1030, 2250),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    16,
    peak_search_range=(0, 2700),
    fitting_range=(790, 950),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    17,
    peak_search_range=(0, 2700),
    fitting_range=(800, 930),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    18,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1030),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    19,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1000),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    20,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1100),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    21,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1170),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    22,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1170),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    23,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1170),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    24,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1000),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    25,
    peak_search_range=(0, 2700),
    fitting_range=(790, 920),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    26,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1170),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    27,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1430),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    28,
    peak_search_range=(0, 2700),
    fitting_range=(870, 1850),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    29,
    peak_search_range=(0, 2700),
    fitting_range=(950, 1850),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    30,
    peak_search_range=(0, 2700),
    fitting_range=(880, 1830),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    31,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1380),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    32,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1100),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    33,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1060),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    34,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1470),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    35,
    peak_search_range=(0, 2700),
    fitting_range=(850, 1600),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    36,
    peak_search_range=(0, 2700),
    fitting_range=(1030, 2110),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    37,
    peak_search_range=(0, 2700),
    fitting_range=(1080, 2210),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    38,
    peak_search_range=(0, 2700),
    fitting_range=(1170, 2470),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    39,
    peak_search_range=(0, 2700),
    fitting_range=(1090, 2150),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    40,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1080),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    41,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1000),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    42,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1440),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    43,
    peak_search_range=(0, 2700),
    fitting_range=(850, 1530),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    44,
    peak_search_range=(0, 2700),
    fitting_range=(1000, 1890),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    45,
    peak_search_range=(0, 2700),
    fitting_range=(950, 1870),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    46,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1210),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    47,
    peak_search_range=(0, 2700),
    fitting_range=(1200, 2450),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    48,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1060),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    49,
    peak_search_range=(0, 2700),
    fitting_range=(780, 1050),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    50,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1300),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    51,
    peak_search_range=(0, 2700),
    fitting_range=(850, 1700),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    52,
    peak_search_range=(0, 2700),
    fitting_range=(980, 1940),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    53,
    peak_search_range=(0, 2700),
    fitting_range=(1050, 2120),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    54,
    peak_search_range=(0, 2700),
    fitting_range=(1250, 2500),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    55,
    peak_search_range=(0, 2700),
    fitting_range=(1300, 2700),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    56,
    peak_search_range=(0, 2700),
    fitting_range=(800, 950),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    57,
    peak_search_range=(0, 2700),
    fitting_range=(800, 920),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    58,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1010),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    59,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1110),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    60,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1270),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    61,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1250),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    62,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1350),
    peak_search_sigma=10
)
cds.get_calb_data("53.3").fit_multi_gaus(
    63,
    peak_search_range=(0, 2700),
    fitting_range=(800, 1350),
    peak_search_sigma=10
)