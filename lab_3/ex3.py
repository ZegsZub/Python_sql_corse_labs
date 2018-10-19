# lab №3 ex. 3 | Var 10 Sergey Zubrilin 10/19/18


import numpy as np
from matplotlib import pyplot as plt


x0 = np.linspace(1, 2, 100)
x1 = np.linspace(2, 3, 100)[1:]
x2 = np.linspace(3, 3.5, 100)[1:]
fig, ax = plt.subplots()
ax.plot(x0, x0**2*(np.log(x0)), label='f(x) = x**x', color='green', ls='--', lw=1.5)
ax.plot(x1, (x1**3)/2, label='g(x) = x**x**X', color='blue', ls='--', lw=1.5)
ax.plot(x2, x2**x2, label='u(x) = 1/1+x', color='red', lw=1.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('title')
ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
fig.savefig('ex3_plot.png', dpi=200, bbox_inches='tight')
plt.show()
