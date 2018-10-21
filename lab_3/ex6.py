# lab №3 ex. 6| Var 10 Sergey Zubrilin 10/19/18


import numpy as np
from matplotlib import pyplot as plt


def fun(x, y):
    return ((x**2+y**2)-3)*np.sqrt(x**2+y**2)+np.sin(8*np.sqrt(x**2+y**2))*np.cos(6*np.arctan(y/np.fabs(x)))-3/4*\
           (np.sin(5*np.arctan(y/np.fabs(x))-1))


x = y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)
fig, ax = plt.subplots()
plt.contour(X, Y, fun(X, Y))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('ex6')
ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
fig.savefig('ex6_plot_a.png', dpi=200, bbox_inches='tight')
plt.show()

plt.imsave(arr=fun(X, Y), fname='ex6_plot_b.png', origin='lower', dpi=600)
plt.show()
