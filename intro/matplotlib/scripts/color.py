import numpy as np
import matplotlib
matplotlib.rcParams['toolbar'] = 'None'
import matplotlib.pyplot as plt


size = 48,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
for i in range(1,8):
    plt.plot( [i,i], [0,1], lw=1.5 )
plt.xlim(0,8)
plt.xticks([]),plt.yticks([])
fig.savefig('../figures/color.png', dpi=dpi)

size = 320,240
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
for i in range(1,8):
    plt.plot( [i,i], [0,1], lw=3 )
plt.xlim(0,8)
plt.xticks([]),plt.yticks([])
fig.savefig('../figures/color-big.png', dpi=dpi)


