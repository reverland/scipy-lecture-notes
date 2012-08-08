from pylab import *

n = 20
Z = np.ones(n)
Z[-1] *= 2
pie(Z, explode=Z*.05, colors = ['%f' % (i/float(n)) for i in range(n)])
gca().set_aspect('equal')
xticks([]), plt.yticks([])
show()
