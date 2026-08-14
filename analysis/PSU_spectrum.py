# -*- coding: utf-8 -*-
"""
Power Supply Noise Spectrum Analysis v1.0

Lukas Kostal, 30.7.2026, Vienna
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sft

# function to average over every n elemnts in an array
def get_avg(arr, n):
    n = int(n)
    arr = arr[(len(arr) % n):]

    arr = np.mean(arr.reshape(-1, n), axis = 1)
    return arr


# measurement to analyze
mes = "BG"

# no of points to average over
n_avg = 2

# path to data
path = "/Users/lukaskostal/Desktop/Masters Project/"

# list of timebase
T_lst = ["100ms", "10ms", "1ms", "100us", "10us"]

# arrays to hold freq, NPSD
f_arr = np.zeros(len(T_lst), dtype=object)
NPSD_arr = np.zeros(len(T_lst), dtype=object)

for i in range(0, len(T_lst)):
    # file to analyze
    file = path + f"data/PSU_noise/{mes}_{T_lst[i]}.CSV"
    
    # load data
    t_arr, V_arr = np.loadtxt(file, delimiter=',', skiprows=16, unpack=True)
    
    # offset time to start at 0 and remove voltage offset
    t_arr = t_arr - t_arr[0]
    V_arr = V_arr - np.mean(V_arr)
    
    # no of samples and sampling frequency
    Ns = len(t_arr)
    Ts = np.mean(np.diff(t_arr))
    fs = 1/Ts
    
    # calculate FFT
    f_fft = sft.rfftfreq(Ns, Ts)[1:]
    V_fft = sft.rfft(V_arr)[1:]
    
    # calculate NPSD
    NPSD = np.abs(V_fft)**2 * 2 / (fs * Ns)
    
    f_arr[i] = f_fft
    NPSD_arr[i] = NPSD
    
# combine NPSD for different timebases
f = np.concatenate(f_arr)
NPSD = np.concatenate(NPSD_arr)
idx = np.argsort(f)
f = f[idx]
NPSD = NPSD[idx]
    
f = get_avg(f, n_avg)
NPSD = get_avg(NPSD, n_avg)

subtitle = "background"

plt.figure(1, figsize=(12, 5))
plt.title(f"Noise Power Spectral Density \n {subtitle}")
plt.xlabel(r"frequency $f$ (Hz)")
plt.ylabel(r"NPSD $S_P$ ($\text{V}^2 \text{Hz}^{-1}$)")
plt.rc('grid', linestyle=':', color='black', alpha=0.8)
plt.grid()

plt.xscale("log")
plt.yscale("log")
plt.xlim((1e1, 1e6))
plt.ylim((1e-16, 1e-6))

plt.plot(f, NPSD, c="b", lw=1)
plt.axvline(50, c="g", ls=":")

file = path + f"/output/NPSD_{mes}.png"
plt.savefig(file, dpi=300, bbox_inches="tight", pad_inches=0.2)

plt.show()