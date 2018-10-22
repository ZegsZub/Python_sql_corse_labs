# lab №3 ex. 7| Var 10 Sergey Zubrilin 10/21/18


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


def fun(x, y):
    return ((y**2)-3)*np.sin(x/(np.fabs(y)+1))


x = np.linspace(-2*np.pi, 2*np.pi)
y = np.linspace(-3, 3)
X, Y = np.meshgrid(x, y)


# поверхностью с линиями уровня
fig = plt.figure(figsize=plt.figaspect(0.4))


ax = fig.add_subplot(121, projection='3d')
p = ax.plot_surface(X, Y, fun(X, Y), cmap=mpl.cm.plasma, rstride=1, cstride=1)
ax.view_init(30, 150)

ax = fig.add_subplot(122, projection='3d')
p = ax.plot_surface(X, Y, fun(X, Y), cmap=mpl.cm.plasma, rstride=1, cstride=1)
cb = fig.colorbar(p, shrink=0.5)
ax.view_init(20, 30)
# fig.tight_layout()

fig.savefig('ex7_plot_a.png', dpi=600)

# каркасной поверхностью
fig = plt.figure(figsize=plt.figaspect(0.4))


ax = fig.add_subplot(121, projection='3d')
p = ax.p = ax.plot_wireframe(X, Y, fun(X, Y), rstride=3, cstride=3)

ax.view_init(30, 150)

ax = fig.add_subplot(122, projection='3d', )
p = ax.p = ax.plot_wireframe(X, Y, fun(X, Y), rstride=3, cstride=3)

ax.view_init(20, 30)

fig.savefig('ex7_plot_b.png', dpi=600)


