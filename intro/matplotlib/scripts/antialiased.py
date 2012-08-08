import numpy as np
import matplotlib
matplotlib.rcParams['toolbar'] = 'None'
import matplotlib.pyplot as plt


size = 48,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
plt.plot([0,1],[0,1], color='b', linewidth=.5)
plt.plot([2,3],[0,1], color='b', linewidth=.5, antialiased=False)
plt.xlim(-1,4)
plt.xticks([]),plt.yticks([])
fig.savefig('../figures/antialiased.png', dpi=dpi)

size = 320,240
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
plt.plot([0,1],[0,1], color='b', linewidth=.5)
plt.plot([2,3],[0,1], color='b', linewidth=.5, antialiased=False)
plt.xlim(-1,4)
plt.xticks([]),plt.yticks([])
fig.savefig('../figures/antialiased-big.png', dpi=dpi)


