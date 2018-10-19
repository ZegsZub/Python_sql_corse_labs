# lab №3 ex. 5 | Var 10 Sergey Zubrilin 10/19/18


import numpy as np
from matplotlib import pyplot as plt

intersection_point = [np.roots([1, 6])[0], np.roots([1, 6])[0]-1]
ip = intersection_point


y = np.linspace(intersection_point[1]-30, intersection_point[1]+30, 100)
x = np.linspace(intersection_point[0]-30, intersection_point[0]+30, 100)
fig, ax = plt.subplots()
ax.plot(y, x-1, color='green', ls='--', lw=1.5)
ax.plot(y, (2*x)+5, color='blue', ls='--', lw=1.5)
ax.plot(intersection_point[1], intersection_point[0],  color='red', marker='o', markersize=5)

ax.text(-30, -16, 'y₁=x-1', fontsize=20, color='green')
ax.text(-30, -60, 'y₂=2x+1', fontsize=20, color='blue')
ax.annotate(f'Q({ip[0]},{ip[1]})', xy=tuple(ip),
            xytext=(ip[0]-20, ip[1]+20), fontsize=15,
            arrowprops=dict(facecolor='black', arrowstyle='->'))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
fig.savefig('ex5_plot.png', dpi=200, bbox_inches='tight')
plt.show()
