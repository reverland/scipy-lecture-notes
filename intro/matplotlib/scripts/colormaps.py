from pylab import *

def colormap(cmap):
    n = 512
    Z = np.linspace(0,1,n,endpoint=True).reshape((1,n))

    size = 128,16
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)
    axes([0.05,0.05,0.9,0.9])
    xticks([]), yticks([])
    imshow(Z,aspect='auto',cmap=cmap,origin="lower")
    savefig( "cmap-%s.png" % cmap, dpi=dpi )


    size = 512,64
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)
    axes([0.01,0.01,0.98,0.98])
    xticks([]), yticks([])
    imshow(Z,aspect='auto',cmap=cmap,origin="lower")
    savefig( "cmap-%s-big.png" % cmap, dpi=dpi )



cmaps = [m for m in cm.datad if not m.endswith("_r")]
cmaps.sort()
print "============= ================================================ "*2
print "Name          Appearance                                       "*2
print "============= ================================================ "*2
for i in range(0,len(cmaps),2):
    #print cmaps[i], cmaps[i+1]
    #colormap(cmap)
    cmap1 = '%-13s'  % cmaps[i]
    link1 = '%-48s'  % (".. image:: figures/cmap-%s.png" % cmaps[i])
    cmap2 = '%-13s'  % cmaps[i+1]
    link2 = '%-48s'  % (".. image:: figures/cmap-%s.png" % cmaps[i+1])

    print cmap1,link1,cmap2,link2

    cmap1 = '%-13s'  % ""
    link1 = '%-48s'  % ("   :target: figures/cmap-%s-big.png" % cmaps[i])
    cmap2 = '%-13s'  % ""
    link2 = '%-48s'  % ("   :target: figures/cmap-%s-big.png" % cmaps[i+1])

    print cmap1,link1,cmap2,link2

    #print "%-13s ..image:: figures/cmap-%s.png" % (cmap,cmap)
    #print "%-13s   :target: figures/cmap-%s-big.png" % ('',cmap)
print "============= ================================================ "*2
