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
    r,g,b = np.random.uniform(0,1,3)
    plt.plot([i,],[1,],'o', markersize=1, markerfacecolor='w',
             markeredgewidth=3, markeredgecolor=(r,g,b,1))
plt.xlim(0,11)
plt.xticks([]),plt.yticks([])
fig.savefig('../figures/mec.png', dpi=dpi)


size = 640,480
dpi = 100.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
for i in range(1,11):
    r,g,b = np.random.uniform(0,1,3)
    plt.plot([i,],[1,],'o', markersize=20, markerfacecolor='w',
             markeredgewidth=5, markeredgecolor=(r,g,b,1))
plt.xlim(0,11)
plt.xticks([]),plt.yticks([])
fig.savefig('../figures/mec-big.png', dpi=dpi/2)


