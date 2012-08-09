from pylab import *

subplot(111,polar=True)

N = 20
theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
radii = 10*np.random.rand(N)
width = np.pi/4*np.random.rand(N)
bars = bar(theta, radii, width=width, bottom=0.0)

for r,bar in zip(radii, bars):
    bar.set_facecolor( cm.jet(r/10.))
    bar.set_alpha(0.5)

gca().set_xticklabels([])
gca().set_yticklabels([])

# savefig('../figures/polar_ex.png',dpi=64)
show()
