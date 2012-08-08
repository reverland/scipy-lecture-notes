import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

size = 48,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
for i in range(1,11):
    plt.plot([i,],[1,],'o', markersize=1,
             markeredgewidth=1+i/10., markeredgecolor='b', markerfacecolor='w')
plt.xlim(0,11)
plt.xticks([]),plt.yticks([])
fig.savefig('../figures/mew.png', dpi=dpi)


size = 640,480
dpi = 100.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
for i in range(1,11):
    plt.plot([i,],[1,],'o', markersize=20,
             markeredgewidth=1+i/2., markeredgecolor='b', markerfacecolor='w')
plt.xlim(0,11)
plt.xticks([]),plt.yticks([])
fig.savefig('../figures/mew-big.png', dpi=dpi/2)


