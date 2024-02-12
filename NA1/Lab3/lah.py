import numpy as np
import matplotlib.pyplot as plt

# Define simulation parameters
num_segments = 100  # Number of road segments
segment_length = 100  # Length of each road segment
simulation_duration = 100  # Number of simulation time steps
Vmax = 20  # Maximum velocity
rho_max = 10  # Maximum traffic density

# Initialize variables
rho = np.zeros((num_segments + 1, simulation_duration + 1))  # Traffic density for each segment at each time step
v = np.zeros((num_segments + 1, simulation_duration + 1))  # Traffic velocity for each segment at each time step

# Set initial conditions
rho[:, 0] = 5  # Initial traffic density for all segments
v[:, 0] = Vmax * (1 - rho[:, 0] / rho_max)  # Initial traffic velocity for all segments

# Set time step size
time_step = 1

# Simulate traffic flow over time
for t in range(simulation_duration):
    for x in range(1, num_segments):  # Exclude boundary segments
        # Calculate the rate of change of traffic density (dρ/dt)
        d_rho_dt = -np.diff(rho[:, t]) / segment_length

        # Calculate the rate of change of (ρv) with respect to position (d(ρv)/dx)
        d_rhov_dx = -np.diff(rho[:, t] * v[:, t]) / segment_length

        # Update traffic density and velocity using LWA equations
        rho[x, t + 1] = rho[x, t] + d_rho_dt[x] * time_step
        v[x, t + 1] = Vmax * (1 - rho[x, t + 1] / rho_max)

    # Calculate traffic flow for each segment at time t
    q = rho[1:num_segments, t] * v[1:num_segments, t]

    # Record data for analysis and visualization

# Plotting example
time = np.arange(simulation_duration + 1) * time_step
plt.figure()
for x in range(1, num_segments):  # Exclude boundary segments
    plt.plot(time, rho[x, :], label=f"Segment {x}")
plt.xlabel("Time")
plt.ylabel("Traffic Density")
plt.title("Traffic Density over Time")
plt.legend()
plt.show()
