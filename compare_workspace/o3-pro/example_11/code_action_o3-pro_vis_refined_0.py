import matplotlib
matplotlib.use('Agg')
# novice_final.py
#
# This script plots two smooth profiles together with an idealized sharp
# interface, fully satisfying the given requirements while relying solely
# on NumPy and Matplotlib.  One PNG file called “novice_final.png” is
# generated; the script never attempts to open an interactive window.

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. Parameters
# -------------------------------------------------
gamma = 1.0   # γ in the phase-field expression
omega = 2.0   # Ω in the composition expression

# -------------------------------------------------
# 2. Domain and profile definitions
# -------------------------------------------------
x = np.linspace(-2.0, 2.0, 400)

phase_field = 0.5 * (1.0 + np.tanh(gamma * x))   # 0.5·[1 + tanh(γx)]
composition = 0.5 * (1.0 + np.tanh(omega * x))   # 0.5·[1 + tanh(Ωx)]

# -------------------------------------------------
# 3. Figure setup and curves
# -------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, phase_field,
        color='blue',
        label=r'Phase Field: $0.5\,[1+\tanh(\gamma x)]$')

ax.plot(x, composition,
        color='orange',
        label=r'Composition: $0.5\,[1+\tanh(\Omega x)]$')

# -------------------------------------------------
# 4. Ideal sharp-interface construction
# -------------------------------------------------
# Vertical line at x = 0
ax.axvline(0.0, color='green', linestyle='-', label='Sharp Interface')

# Horizontal segments showing ideal jump
ax.plot([-2.0,  0.0], [0.0, 0.0], color='green', linestyle='--')
ax.plot([ 0.0,  2.0], [1.0, 1.0], color='green', linestyle='--')

# -------------------------------------------------
# 5. Text annotations
# -------------------------------------------------
ax.text(-1.5, 0.8,
        r'Phase Field: $\,\tfrac12 (1+\tanh(\gamma x))$',
        color='blue')

ax.text(-1.5, 0.2,
        r'Composition: $\,\tfrac12 (1+\tanh(\Omega x))$',
        color='orange')

ax.text(-1.85, 0.92,
        r'$\gamma = 1.0$' '\n' r'$\Omega = 2.0$',
        fontsize=12)

# Arrow pointing to the intersection of the two smooth curves
ax.annotate('Intersection',
            xy=(0.0, 0.5),
            xytext=(-1.0, 0.6),
            arrowprops=dict(facecolor='black', shrink=0.05))

# -------------------------------------------------
# 6. Axes labels, limits, legend
# -------------------------------------------------
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(-2.0, 2.0)
ax.set_ylim(0.0, 1.0)
ax.legend(loc='upper left')

# -------------------------------------------------
# 7. Finalize: save exactly one PNG (no interactive show)
# -------------------------------------------------
plt.tight_layout()
plt.savefig("novice_final.png")