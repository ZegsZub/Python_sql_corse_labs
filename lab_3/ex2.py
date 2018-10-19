# lab №2 ex. 1 | Var 4 Sergey Zubrilin 10/3/18


import numpy as np
from matplotlib import pyplot as plt


# в одно окно на одни оси
fi = np.linspace(0, 2*np.pi, 400)
fig = plt.figure()
fig.set_tight_layout(False)


def fun(f):
    return 2-(2*np.sin(f))+(np.sin(f))*(np.sqrt(np.fabs(np.cos(f)))/(np.sin(f)+1.4))


ax = fig.add_axes([0.0, 0.0, 1, 1], polar=True)

ax.plot(fi, fun(fi), color='red', ls='', lw=3, marker='o', markersize=2)
fig.savefig('ex2_plot.png', dpi=500, bbox_inches='tight')
plt.show()
