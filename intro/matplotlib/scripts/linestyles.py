import numpy as np
import matplotlib
matplotlib.rcParams['toolbar'] = 'None'
import matplotlib.pyplot as plt


def linestyle(ls):
    size = 48,16
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)
    X = np.arange(5)
    Y = np.ones(5)
    plt.plot(X,Y,ls)
    plt.xlim(0,4)
    plt.xticks([]),plt.yticks([])
    fig.savefig('linestyle-%s.png' % ls, dpi=dpi)

    size = 320,240
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)
    X = np.linspace(0,1,50,endpoint=True)
    Y = np.sin(X*2*np.pi)
    plt.plot(X,Y,ls,lw=3)
    plt.xlim(0,1), plt.ylim(-1.1,1.1)
    plt.xticks([]),plt.yticks([])
    fig.savefig('linestyle-%s-big.png' % ls, dpi=dpi)


for ls in ['-','--','-.',':','.',',','o','^','v','<','>','s',
           '+','x','D','d','1','2','3','4','h','H','p','|','_']:
    linestyle(ls)
