import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(z):
    return (z - 4) * (z - 6) * (z - 8) + 90

z = np.linspace(0, 11, 400)
y = f(z)

plt.figure(figsize=(8, 6))
plt.plot(z, y, color='blue', linewidth=2)
plt.fill_between(z, y, where=(z >= 3) & (z <= 10), color='lightblue', alpha=0.5)
plt.text(6.5, 50, r'$\int (z - 4)(z - 6)(z - 8) + 90 \, dz$', fontsize=12, ha='center')
plt.xlim(0, 11)
plt.ylim(bottom=0)
plt.xlabel('z')
plt.ylabel('y')
plt.xticks([3, 10], ['3', '10'])
plt.yticks([])
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.savefig('novice_final.png', bbox_inches='tight')