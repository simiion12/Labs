import numpy as np
import matplotlib.pyplot as plt

# Define the initial conditions
U0 = 0.0  # Initial resource utilisation
R0 = 100.0  # Initial total available resources

# Define the arrival rate and departure rate functions
def arrival_rate(t):
    return 10.0  # Example constant arrival rate

def departure_rate(t, U):
    return 0.1 * U  # Example departure rate proportional to resource utilisation

# Define the ODEs
def dU_dt(U, t):
    return arrival_rate(t) - departure_rate(t, U)

def dR_dt(R, U, t):
    return arrival_rate(t) - departure_rate(t, U)

# Solve the ODEs using Euler's method
def solve_odes_euler(U0, R0, dt, num_steps):
    U = np.zeros(num_steps)
    R = np.zeros(num_steps)
    U[0] = U0
    R[0] = R0

    for i in range(1, num_steps):
        U[i] = U[i-1] + dt * dU_dt(U[i-1], i*dt)
        R[i] = R[i-1] + dt * dR_dt(R[i-1], U[i-1], i*dt)

    return U, R

# Set the time step and number of steps
dt = 0.1  # Time step
num_steps = 100  # Number of steps

# Solve the ODEs
U, R = solve_odes_euler(U0, R0, dt, num_steps)

# Plot the results
time = np.arange(0, num_steps * dt, dt)
plt.plot(time, U, label='Resource Utilisation')
plt.plot(time, R, label='Total Available Resources')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
