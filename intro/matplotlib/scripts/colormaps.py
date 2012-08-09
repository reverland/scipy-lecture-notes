from pylab import *

def colormap(cmap):
    n = 512
    Z = np.linspace(0,1,n,endpoint=True).reshape((1,n))
    size = 512,16
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)
    axes([0.,0.,1.,1.], frameon=False)
    xticks([]), yticks([])
    imshow(Z,aspect='auto',cmap=cmap,origin="lower")
    savefig( "../figures/cmap-%s.png" % cmap, dpi=dpi )

    """
    size = 512,64
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)
    axes([0.01,0.01,0.98,0.98])
    xticks([]), yticks([])
    imshow(Z,aspect='auto',cmap=cmap,origin="lower")
    savefig( "cmap-%s-big.png" % cmap, dpi=dpi )
    """


cmaps = [m for m in cm.datad if not m.endswith("_r")]
cmaps.sort()

print """
.. list-table::
   :widths: 10 30 50
   :header-rows: 1

   * - Name
     - Description
     - Appearance

"""

for i in range(len(cmaps)):
    # colormap(cmaps[i])
    print "   * - %s" %cmaps[i]
    print "     - " 
    print "     - .. image:: figures/cmap-%s.png" % cmaps[i]
    print

