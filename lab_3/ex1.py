# lab №2 ex. 1 | Var 4 Sergey Zubrilin 10/3/18


import numpy as np
from matplotlib import pyplot as plt


# в одно окно на одни оси
x = np.linspace(0.01, 1, 10)
fig, ax = plt.subplots()
ax.plot(x, x**x, label='f(x) = x**x', color='green', ls='--', lw=1.5, marker='*')
ax.plot(x, x**x**x, label='g(x) = x**x**X', color='blue', ls='--', lw=1.5, marker='*')
x = np.linspace(0, 1)
ax.plot(x, 1/(1+x), label='u(x) = 1/1+x', color='red', ls='-.', lw=1.5, marker='o', markersize=5)
ax.plot(x, 1/(1+(1/(1+x))), label='v(x) = 1/1+(1/(1+x))', color='black', ls='-.', lw=1.5, marker='o', markersize=5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('title')
ax.legend(loc=0)
ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
fig.savefig('ex1_plot_a.png', dpi=200, bbox_inches='tight')
plt.show()

# в одно окно на отдельные оси
fig, ax = plt.subplots(2, 2)
x = np.linspace(0.01, 1, 10)
ax[0, 0].plot(x, x**x, label='f(x) = x**x', color='green', ls='--', lw=1.5, marker='*')
ax[0, 1].plot(x, x**x**x, label='g(x) = x**x**X', color='blue', ls='--', lw=1.5, marker='*')
x = np.linspace(0, 1)
ax[1, 0].plot(x, 1/(1+x), label='u(x) = 1/1+x', color='red', ls='-.', lw=1.5, marker='o', markersize=2)
ax[1, 1].plot(x, 1/(1+(1/(1+x))), label='v(x) = 1/1+(1/(1+x))', color='black', ls='-.', lw=1.5, marker='o',
              markersize=2)
fig.tight_layout()
plt.subplots_adjust(left=None, bottom=None, right=1.2, top=1.2, wspace=0.3, hspace=0.3)

for i in range(2):
    for j in range(2):
        ax[i, j].set_xlabel('X')
        ax[i, j].set_ylabel('Y')
        ax[i, j].set_title('title')
        ax[i, j].legend(loc=0)
        ax[i, j].grid(color='b', alpha=1, linestyle='dashed', linewidth=0.5)

fig.savefig('ex1_plot_b.png', dpi=200, bbox_inches='tight')
plt.show()

