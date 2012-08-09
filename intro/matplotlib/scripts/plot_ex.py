from pylab import *

n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)

plot (X, Y+1, color='blue', alpha=1.00)
fill_between(X, 1, Y+1, color='blue', alpha=.25)

plot (X, Y-1, color='blue', alpha=1.00)
fill_between(X, -1, Y-1, (Y-1) > -1, color='blue', alpha=.25)
fill_between(X, -1, Y-1, (Y-1) < -1, color='red',  alpha=.25)


xlim(-np.pi,np.pi), xticks([])
ylim(-2.5,2.5), yticks([])
#savefig('../figures/plot_ex.png',dpi=64)
show()
