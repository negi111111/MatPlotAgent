import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # noqa: F401  (needed for 3-D plotting even if unused directly)

# -------------------------------------------------
# 1. Define g(s) and generate its data
# -------------------------------------------------
def g(s):
    """Damped sine wave: g(s) = sin(3πs) * e^(−s)."""
    return np.sin(3 * np.pi * s) * np.exp(-s)

s = np.linspace(0, 2, 100)
g_s          = g(s)
g_s_plus_01  = g(s + 0.1)
g_s_plus_02  = g(s + 0.2)

# -------------------------------------------------
# 2. Define E(P, Q) and generate its data
# -------------------------------------------------
def E(P, Q):
    """Radial cosine surface: E(P, Q) = cos(√(P² + Q²))."""
    return np.cos(np.sqrt(P**2 + Q**2))

P_vals = np.linspace(-5, 5, 100)
Q_vals = np.linspace(-5, 5, 100)
P, Q   = np.meshgrid(P_vals, Q_vals)
E_vals = E(P, Q)

# -------------------------------------------------
# 3. Create the figure with two subplots
# -------------------------------------------------
fig = plt.figure(figsize=(12, 6))

# --- 2-D subplot for g(s) -------------------------------------
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(s, g_s,           label='g(s)',        color='blue')
ax1.plot(s, g_s_plus_01,   label='g(s + 0.1)',  linestyle='--', color='red')
ax1.plot(s, g_s_plus_02,   label='g(s + 0.2)',  linestyle=':',  color='green')
ax1.set_title('Damped sine waves')
ax1.set_xlabel('s')
ax1.set_ylabel('g(s)')
ax1.legend()

# --- 3-D surface subplot for E(P, Q) ---------------------------
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf = ax2.plot_surface(P, Q, E_vals, cmap='viridis', linewidth=0, antialiased=False)
ax2.set_title('E(P, Q) = cos(√(P² + Q²))')
ax2.set_xlabel('P')
ax2.set_ylabel('Q')
ax2.set_zlabel('E value')
fig.colorbar(surf, ax=ax2, shrink=0.6, aspect=12)

# -------------------------------------------------
# 4. Global title and save
# -------------------------------------------------
fig.suptitle('A Story of 2 Subplots', fontsize=14, y=0.95)
plt.tight_layout(rect=[0, 0, 1, 0.94])   # leave space for suptitle
plt.savefig('novice_final.png')           # exactly one PNG saved