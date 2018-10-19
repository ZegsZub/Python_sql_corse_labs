# lab №3 ex. 4 | Var 10 Sergey Zubrilin 10/19/18


import numpy as np
from matplotlib import pyplot as plt


def f1(t):
    return np.sin(t) + (3*np.cos(t) - np.sin(3*t)/4)


def f2(t):
    return np.sin(t) * np.cos(t)


t = np.linspace(0, 2*np.pi, 50)
fig, ax = plt.subplots()
ax.plot(f1(t), f2(t), color='green', ls='--', lw=1.5)

fig.savefig('ex4_plot.png', dpi=200, bbox_inches='tight')
plt.show()
