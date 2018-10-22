# lab №3 ex. 8 | Var 10 Sergey Zubrilin 10/22/18


import numpy as np
import matplotlib.pyplot as plt

r = 2 # заданная в условии r
q = r/np.sqrt(2)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)
plt.gca().set_aspect('equal', adjustable='box')
ax.set_xlim(-2.1, 2.1)
ax.set_ylim(-2.1, 2.1)
rect = plt.Rectangle((-q, -q), q*2, q*2, fill=False, lw=2)
circ = plt.Circle((0.0, 0.0), r, fill=False, lw=2)
ax.add_patch(rect)
ax.add_patch(circ)
plt.show()
fig.savefig('ex8_plot.png', dpi=400, bbox_inches='tight')