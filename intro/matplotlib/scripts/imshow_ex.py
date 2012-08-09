from pylab import *

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 10
x = np.linspace(-3,3,4*n)
y = np.linspace(-3,3,3*n)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
imshow(Z,interpolation='nearest', cmap='bone', origin='lower')
colorbar()

xticks([]), yticks([])
# savefig('../figures/imshow_ex.png', dpi=64)
show()
