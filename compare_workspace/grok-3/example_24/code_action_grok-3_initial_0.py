import matplotlib
matplotlib.use('Agg')
# Import necessary libraries
import numpy as np  # For numerical operations and array handling
from scipy.integrate import solve_ivp  # For solving ordinary differential equations
import matplotlib.pyplot as plt  # For plotting
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

# Define the Rossler attractor equations
def rossler(t, state, a=0.2, b=0.2, c=5.7):
    """
    Define the Rossler attractor system of ODEs.
    Parameters:
        t (float): Time variable (required by solve_ivp, though not used in equations).
        state (list): Current state of the system [u, v, w].
        a, b, c (float): Parameters of the Rossler system.
    Returns:
        list: Derivatives [du/dt, dv/dt, dw/dt].
    """
    u, v, w = state
    du_dt = -v - w
    dv_dt = u + a * v
    dw_dt = b + w * (u - c)
    return [du_dt, dv_dt, dw_dt]

# Set up the time span and initial conditions
t_span = (0, 100)  # Time range for integration (from 0 to 100)
t_eval = np.linspace(0, 100, 10000)  # Points at which to evaluate the solution (fine grid for smooth plot)
initial_conditions = [1.0, 1.0, 1.0]  # Initial values for u, v, w as specified

# Solve the ODEs using solve_ivp
solution = solve_ivp(
    fun=rossler,  # The function defining the ODE system
    t_span=t_span,  # The time interval for integration
    y0=initial_conditions,  # Initial conditions
    t_eval=t_eval,  # Points at which to evaluate the solution
    method='RK45'  # Runge-Kutta method for numerical integration
)

# Extract the solution data for plotting
u = solution.y[0]  # Solution for u over time
v = solution.y[1]  # Solution for v over time
w = solution.y[2]  # Solution for w over time

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))  # Create a figure with specified size for better visibility
ax = fig.add_subplot(111, projection='3d')  # Add a 3D subplot to the figure

# Plot the trajectory in 3D space with a high-contrast color
ax.plot(
    u, v, w,  # Data for the three axes
    linewidth=0.5,  # Set line width to 0.5 as specified
    color='blue'  # Use a clear, high-contrast color
)

# Customize the plot
ax.set_xlabel('u')  # Label for the x-axis
ax.set_ylabel('v')  # Label for the y-axis
ax.set_zlabel('w')  # Label for the z-axis
ax.set_title('Rossler Attractor')  # Set the title as specified

# Save the plot as a PNG file
plt.savefig("novice.png")