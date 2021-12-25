from make_hitmap import fetch_calibration_functions
import matplotlib.pyplot as plt

calibration_parameters, _, _ = fetch_calibration_functions()
print(calibration_parameters)
channels = []
adc_par_photons = []

for k, v in calibration_parameters.items():
    channel = k
    adc_par_photon = v[0]
    channels.append(channel)
    adc_par_photons.append(adc_par_photon)
    
figure = plt.figure()
plt.scatter(list(range(16)), adc_par_photons)
plt.xticks(list(range(16)), channels)
plt.title("Difference in ADC value per channel")
plt.xlabel("Channel")
plt.ylabel("ADC Count / Photon Number")
print(calibration_parameters)
figure.savefig("8x2array/img/make_ch_vs_adc_par_photon.png")