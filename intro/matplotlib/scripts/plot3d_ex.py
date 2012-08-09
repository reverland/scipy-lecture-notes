from pylab import *
from mpl_toolkits.mplot3d import axes3d

ax = gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
cset = ax.contourf(X, Y, Z)
xticks([]), yticks([]), ax.set_zticks([])

# savefig('../figures/plot3d_ex.png',dpi=64)
show()
