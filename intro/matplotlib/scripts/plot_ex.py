from pylab import *

n = 256
X = np.linspace(0,2,n)
Y = np.sin(2*np.pi*X)
plt.plot (X, Y, lw=2, color='violet')
xlim(-0.2,2.2), xticks([])
ylim(-1.2,1.2), yticks([])
