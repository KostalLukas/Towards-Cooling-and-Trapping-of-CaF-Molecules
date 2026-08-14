# -*- coding: utf-8 -*-
"""
Power Supply Switching Analysis v1.0

Lukas Kostal, 12.8.2026, Vienna
"""


import numpy as np
import matplotlib.pyplot as plt


# path to project
path = "/Users/lukaskostal/Desktop/Masters Project/"

# array of currents
I_arr = np.array([20, 40, 60, 80, 100])

# colormap for plotting
cmap = plt.cm.cool(I_arr / np.amax(I_arr))

# setup plotting PS1 CV ON
plt.figure(1, figsize=(8, 5))
plt.title("SM30-200 CV Mode Switching ON")
plt.xlabel("time $t$ (ms)")
plt.ylabel("voltage $V$ (V)")
plt.rc('grid', linestyle=':', color='black', alpha=0.8)
plt.grid()

# loop over currents and plot
for i in range(0, len(I_arr)):
    file = path + f"data/PSU_switch/PSU1_CV_{I_arr[i]}A_ON.CSV"
    
    
    t_arr, V_arr = np.loadtxt(file, delimiter=',', skiprows=16, unpack=True)
    t_arr = t_arr - t_arr[0] - 20e-3
    
    plt.plot(t_arr*1e3, V_arr, lw=1, c=cmap[i], zorder=-i, label=f"{I_arr[i]:.0f} A")
    
plt.xlim(0, 80)
plt.legend()

# save plot
file = path + "/output/PSU_switch_PSU1_CV_ON.png"
plt.savefig(file, dpi=300, bbox_inches="tight", pad_inches=0.2)
plt.show()

# setup plotting PS1 CV OFF
plt.figure(1, figsize=(8, 5))
plt.title("SM30-200 CV Mode Switching OFF")
plt.xlabel("time $t$ (ms)")
plt.ylabel("voltage $V$ (V)")
plt.rc('grid', linestyle=':', color='black', alpha=0.8)
plt.grid()

# loop over currents and plot
for i in range(0, len(I_arr)):
    file = path + f"data/PSU_switch/PSU1_CV_{I_arr[i]}A_OFF.CSV"
    
    t_arr, V_arr = np.loadtxt(file, delimiter=',', skiprows=16, unpack=True)
    t_arr = t_arr - t_arr[0] - 20e-3
    
    plt.plot(t_arr*1e3, V_arr, lw=1, c=cmap[i], zorder=-i, label=f"{I_arr[i]:.0f} A")
    
plt.xlim(0, 80)
plt.legend()

# save plot
file = path + "/output/PSU_switch_PSU1_CV_OFF.png"
plt.savefig(file, dpi=300, bbox_inches="tight", pad_inches=0.2)
plt.show()

# setup plotting PS1 CC ON
plt.figure(1, figsize=(8, 5))
plt.title("SM30-200 CC Mode Switching ON")
plt.xlabel("time $t$ (ms)")
plt.ylabel("voltage $V$ (V)")
plt.rc('grid', linestyle=':', color='black', alpha=0.8)
plt.grid()

# loop over currents and plot
for i in range(0, len(I_arr)):
    file = path + f"data/PSU_switch/PSU1_CC_{I_arr[i]}A_ON.CSV"
    
    t_arr, V_arr = np.loadtxt(file, delimiter=',', skiprows=16, unpack=True)
    t_arr = t_arr - t_arr[0] - 20e-3
    
    plt.plot(t_arr*1e3, V_arr, lw=1, c=cmap[i], zorder=-i, label=f"{I_arr[i]:.0f} A")
    
plt.xlim(0, 80)
plt.legend()

# save plot
file = path + "/output/PSU_switch_PSU1_CC_ON.png"
plt.savefig(file, dpi=300, bbox_inches="tight", pad_inches=0.2)
plt.show()

# setup plotting PS1 CC OFF
plt.figure(1, figsize=(8, 5))
plt.title("SM30-200 CC Mode Switching OFF")
plt.xlabel("time $t$ (ms)")
plt.ylabel("voltage $V$ (V)")
plt.rc('grid', linestyle=':', color='black', alpha=0.8)
plt.grid()

# loop over currens and plot
for i in range(0, len(I_arr)):
    file = path + f"data/PSU_switch/PSU1_CC_{I_arr[i]}A_OFF.CSV"
    
    t_arr, V_arr = np.loadtxt(file, delimiter=',', skiprows=16, unpack=True)
    t_arr = t_arr - t_arr[0] - 20e-3
    
    plt.plot(t_arr*1e3, V_arr, lw=1, c=cmap[i], zorder=-i, label=f"{I_arr[i]:.0f} A")
    
plt.xlim(0, 80)
plt.legend()

# save plot
file = path + "/output/PSU_switch_PSU1_CC_OFF.png"
plt.savefig(file, dpi=300, bbox_inches="tight", pad_inches=0.2)
plt.show()

# setup plotting PS2 CV ON
plt.figure(1, figsize=(8, 5))
plt.title("SM40-450 CV Mode Switching ON")
plt.xlabel("time $t$ (ms)")
plt.ylabel("voltage $V$ (V)")
plt.rc('grid', linestyle=':', color='black', alpha=0.8)
plt.grid()

# loop over currents and plot
for i in range(0, len(I_arr)):
    file = path + f"data/PSU_switch/PSU2_CV_{I_arr[i]}A_ON.CSV"
    
    t_arr, V_arr = np.loadtxt(file, delimiter=',', skiprows=16, unpack=True)
    t_arr = t_arr - t_arr[0] - 20e-3
    
    plt.plot(t_arr*1e3, V_arr, lw=1, c=cmap[i], zorder=-i, label=f"{I_arr[i]:.0f} A")
    
plt.xlim(0, 80)
plt.legend()

# save plot
file = path + "/output/PSU_switch_PSU2_CV_ON.png"
plt.savefig(file, dpi=300, bbox_inches="tight", pad_inches=0.2)
plt.show()

# setup plotting PS2 CV OFF
plt.figure(1, figsize=(8, 5))
plt.title("SM40-450 CV Mode Switching OFF")
plt.xlabel("time $t$ (ms)")
plt.ylabel("voltage $V$ (V)")
plt.rc('grid', linestyle=':', color='black', alpha=0.8)
plt.grid()

# loop over currents and plot
for i in range(0, len(I_arr)):
    file = path + f"data/PSU_switch/PSU2_CV_{I_arr[i]}A_OFF.CSV"
    
    t_arr, V_arr = np.loadtxt(file, delimiter=',', skiprows=16, unpack=True)
    t_arr = t_arr - t_arr[0] - 20e-3
    
    plt.plot(t_arr*1e3, V_arr, lw=1, c=cmap[i], zorder=-i, label=f"{I_arr[i]:.0f} A")
    
plt.xlim(0, 80)
plt.legend()

# save plot
file = path + "/output/PSU_switch_PSU2_CV_OFF.png"
plt.savefig(file, dpi=300, bbox_inches="tight", pad_inches=0.2)
plt.show()

# setup plotting PS2 CC ON
plt.figure(1, figsize=(8, 5))
plt.title("SM40-450 CC Mode Switching ON")
plt.xlabel("time $t$ (ms)")
plt.ylabel("voltage $V$ (V)")
plt.rc('grid', linestyle=':', color='black', alpha=0.8)
plt.grid()

# loop over currents and plot
for i in range(0, len(I_arr)):
    file = path + f"data/PSU_switch/PSU2_CC_{I_arr[i]}A_ON.CSV"
    
    t_arr, V_arr = np.loadtxt(file, delimiter=',', skiprows=16, unpack=True)
    t_arr = t_arr - t_arr[0] - 20e-3
    
    plt.plot(t_arr*1e3, V_arr, lw=1, c=cmap[i], zorder=-i, label=f"{I_arr[i]:.0f} A")
    
plt.xlim(0, 260)
plt.legend()

# save plot
file = path + "/output/PSU_switch_PSU2_CC_ON.png"
plt.savefig(file, dpi=300, bbox_inches="tight", pad_inches=0.2)
plt.show()

# setup plotting PS2 CC OFF
plt.figure(1, figsize=(8, 5))
plt.title("SM40-450 CC Mode Switching OFF")
plt.xlabel("time $t$ (ms)")
plt.ylabel("voltage $V$ (V)")
plt.rc('grid', linestyle=':', color='black', alpha=0.8)
plt.grid()

# loop over currents and plot
for i in range(0, len(I_arr)):
    file = path + f"data/PSU_switch/PSU2_CC_{I_arr[i]}A_OFF.CSV"
    
    t_arr, V_arr = np.loadtxt(file, delimiter=',', skiprows=16, unpack=True)
    t_arr = t_arr - t_arr[0] - 20e-3
    
    if(i == 0):
        t_arr += 8e-3
    
    plt.plot(t_arr*1e3, V_arr, lw=1, c=cmap[i], zorder=-i, label=f"{I_arr[i]:.0f} A")
    
plt.xlim(0,80)
plt.legend()

# save plot
file = path + "/output/PSU_switch_PSU2_CC_OFF.png"
plt.savefig(file, dpi=300, bbox_inches="tight", pad_inches=0.2)
plt.show()