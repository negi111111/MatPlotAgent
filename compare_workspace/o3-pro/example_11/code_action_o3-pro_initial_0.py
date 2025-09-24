import matplotlib
matplotlib.use('Agg')
"""
Plot tanh phase-field and composition profiles together with a sharp-interface
reference.  The resulting figure is written to the file ``novice.png``.
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1. Model parameters
# ------------------------------------------------------------------
gamma = 1.0        # γ – phase-field transition width parameter
omega = 2.0        # Ω – composition transition width parameter

# ------------------------------------------------------------------
# 2. Coordinate grid
# ------------------------------------------------------------------
x = np.linspace(-2, 2, 500)          # 500 evenly–spaced points

# ------------------------------------------------------------------
# 3. Profiles
# ------------------------------------------------------------------
y_phase = 0.5 * (1 + np.tanh(gamma * x))   # phase-field profile
y_comp  = 0.5 * (1 + np.tanh(omega * x))   # composition profile

# ------------------------------------------------------------------
# 4. Figure setup
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 4))

# 4a. Smooth tanh curves
ax.plot(x, y_phase, color='blue',   lw=2,
        label=r'Phase Field, $0.5\,[1+\tanh(\gamma x)]$')
ax.plot(x, y_comp,  color='orange', lw=2,
        label=r'Composition, $0.5\,[1+\tanh(\Omega x)]$')

# 4b. Ideal sharp interface (green)
ax.axvline(0, color='green', lw=2, label='Sharp Interface')
ax.hlines(y=0, xmin=-2, xmax=0, color='green', lw=2)
ax.hlines(y=1, xmin=0,  xmax=2, color='green', lw=2)

# ------------------------------------------------------------------
# 5. Text annotations
# ------------------------------------------------------------------
x_text_left = -1.5
# helper index closest to x_text_left
idx_left = np.argmin(np.abs(x - x_text_left))

ax.text(x_text_left,
        y_phase[idx_left] + 0.05,
        r'Phase Field: $0.5\,(1+\tanh(\gamma x))$',
        color='blue')

ax.text(x_text_left,
        y_comp[idx_left] + 0.15,
        r'Composition: $0.5\,(1+\tanh(\Omega x))$',
        color='orange')

# parameter values in upper-left corner
ax.text(-1.9, 0.9,
        r'$\gamma = 1.0$' '\n' r'$\Omega = 2.0$',
        color='black')

# arrow to intersection point
ax.annotate('Intersection',
            xy=(0, 0.5),           # arrow head (intersection)
            xytext=(0.6, 0.7),     # text position
            arrowprops=dict(arrowstyle='->', color='black'))

# ------------------------------------------------------------------
# 6. Aesthetics
# ------------------------------------------------------------------
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(-2, 2)
ax.set_ylim(0, 1)
ax.legend(loc='upper left')
ax.grid(True, ls='--', alpha=0.3)

plt.tight_layout()

# ------------------------------------------------------------------
# 7. Save figure
# ------------------------------------------------------------------
plt.savefig("novice.png", dpi=300)