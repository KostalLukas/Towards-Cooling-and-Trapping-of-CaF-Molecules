# -*- coding: utf-8 -*-
"""
Power Supply RMS Noise Analysis v1.0

Lukas Kostal, 30.7.2026, Vienna
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sft
    

# lowest freq and bandwidth for RMS noise calculation
fi=10
B=300e3

# list of measurements
mes_lst = ["PSU1_CV1", "PSU1_CV2", "PSU1_CC1", "PSU1_CC2", "PSU2_CV1", "PSU2_CV2", "PSU2_CC1", "PSU2_CC2"]


# path to data
path = "/Users/lukaskostal/Desktop/Masters Project/"

# list of timebase and current
T_lst = ["100ms", "10ms", "1ms", "100us", "10us"]
I_lst = ["0A","20A", "40A", "60A", "80A", "100A"]

# arrays to hold freq, NPSD, Vrms and current
f_arr = np.zeros(len(T_lst), dtype=object)
NPSD_arr = np.zeros(len(T_lst), dtype=object)
Vrms_arr = np.zeros((len(mes_lst), len(I_lst)))
I_arr = np.array([0, 20, 40, 60, 80, 100])

# setup plot
plt.figure(1, figsize=(8, 5))
plt.title("Voltage Noise against Current")
plt.xlabel("current $I$ (A)")
plt.ylabel(r"voltage noise $V_\text{RMS}$ (mV)")
plt.rc('grid', linestyle=':', color='black', alpha=0.8)
plt.grid()

# loop over timebase for background measurement
for i in range(0, len(T_lst)):
    # file to analyze
    file = path + f"data/PSU_noise/BG_{T_lst[i]}.CSV"
    
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

# calculate Vrms for values within bandwidth 
idx = np.where(np.logical_and(fi<f, f < B+fi))[0]
Vrms_bg = np.sqrt(np.trapz(NPSD[idx], f[idx]))

# plot background
plt.axhline(Vrms_bg*1e3, c="g", label="background")

# loop over measurement
for i in range(0, len(mes_lst)):
    # loop over current
    for j in range(0, len(I_lst)):
        # loop over timebase
        for k in range(0, len(T_lst)):
            
            file = path + f"data/PSU_noise/{mes_lst[i]}_{I_lst[j]}_{T_lst[k]}.CSV"
            t_arr, V_arr = np.loadtxt(file, delimiter=',', skiprows=16, unpack=True)
            
            t_arr = t_arr - t_arr[0]
            V_arr = V_arr - np.mean(V_arr)
            
            Ns = len(t_arr)
            Ts = np.mean(np.diff(t_arr))
            fs = 1/Ts
            
            f_fft = sft.rfftfreq(Ns, Ts)[1:]
            V_fft = sft.rfft(V_arr)[1:]
            
            NPSD = np.abs(V_fft)**2 * 2 / (fs * Ns)
            
            f_arr[k] = f_fft
            NPSD_arr[k] = NPSD
            
        f = np.concatenate(f_arr)
        NPSD = np.concatenate(NPSD_arr)
        idx = np.argsort(f)
        f = f[idx]
        NPSD = NPSD[idx]
            
        idx = np.where(np.logical_and(fi<f, f < B+fi))[0]
        Vrms = np.sqrt(np.trapz(NPSD[idx], f[idx]))
        
        Vrms_arr[i, j] = Vrms

    # plot
    if ("PSU1" in mes_lst[i]):
        c_plt = "r"
        n_plt = "SM30-200"
    else:
        c_plt = "b"
        n_plt = "SM40-450"

    if ("CC" in mes_lst[i]):
        l_plt = "--"
        n_plt += " CC"
    else:
        l_plt = "-"
        n_plt += " CV"
        
    if (i % 2 == 0):
        plt.plot(I_arr, Vrms_arr[i, :]*1e3, c=c_plt, ls=l_plt, marker=".", lw=1, label=n_plt)
    else:
        plt.plot(I_arr, Vrms_arr[i, :]*1e3, c=c_plt, ls=l_plt, marker=".", lw=1)

plt.legend()

file = path + "/output/PSU_noise.png"
plt.savefig(file, dpi=300, bbox_inches="tight", pad_inches=0.2)
plt.show()    