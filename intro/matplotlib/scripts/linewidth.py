import numpy as np
import matplotlib
matplotlib.rcParams['toolbar'] = 'None'
import matplotlib.pyplot as plt


size = 48,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
for i in range(1,11):
    plt.plot( [i,i], [0,1], color='b', lw=i/4. )
plt.xlim(0,11)
plt.xticks([]),plt.yticks([])
fig.savefig('../figures/linewidth.png', dpi=dpi)

size = 320,240
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
for i in range(1,11):
    plt.plot( [i,i], [0,1], color='b', lw=i )
plt.xlim(0,11)
plt.xticks([]),plt.yticks([])
fig.savefig('../figures/linewidth-big.png', dpi=dpi)


