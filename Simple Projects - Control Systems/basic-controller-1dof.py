import numpy as np
import matplotlib.pyplot as plt
import control as ctl
from scipy.signal import find_peaks
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import os

# === SYSTEM PARAMETERS === #
I = 5  # Moment of inertia
Kp = 10  # Proportional gain

# Define system transfer function
G = ctl.tf([1], [I, 0, 0])  # Plant: 1/(I * s^2)
T = ctl.feedback(Kp * G)  # Closed-loop system

# Time vector
t = np.linspace(0, 10, 1000)

# Step response
t, y = ctl.step_response(T, t)  # y is the angle θ(t)

# === COMPUTE METRICS === #
y_final = y[-1]  # Final steady-state value
tolerance = 0.02 * y_final  # 2% threshold
settling_index = np.where(abs(y - y_final) <= tolerance)[0][0]
settling_time = t[settling_index]

peak_indices, _ = find_peaks(y)
overshoot = ((y[peak_indices[0]] - y_final) / y_final) * 100 if peak_indices.size > 0 else 0
steady_state_error = abs(1 - y_final)

# Print results
print(f"Settling Time: {settling_time:.2f} s")
print(f"Overshoot: {overshoot:.2f}%")
print(f"Steady-State Error: {steady_state_error:.4f}")



# Step Response Plot
plt.figure()
plt.xlabel("Time (s)")
plt.ylabel("Angle θ (rad)")
plt.title("Step Response")
plt.plot(t, y, label=f"Kp={Kp}")
plt.grid()
plt.savefig("single_step_response.png", dpi=300)  # 🔽 Save as PNG
plt.show()


# === 3D SPACECRAFT VISUALIZATION === #
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])
ax.set_zlim([-1.2, 1.2])
ax.set_title("Spacecraft Rotation Visualization")

# Spacecraft body (cuboid)
body_x = np.array([-0.5, 0.5, 0.5, -0.5, -0.5]) * 0.3
body_y = np.array([-0.2, -0.2, 0.2, 0.2, -0.2]) * 0.3
body_z = np.array([0, 0, 0, 0, 0])

# Initial spacecraft plot
spacecraft, = ax.plot(body_x, body_y, body_z, 'bo-', markersize=8, lw=2)

# Add stars in background
num_stars = 50
ax.scatter(np.random.uniform(-1, 1, num_stars), 
           np.random.uniform(-1, 1, num_stars), 
           np.random.uniform(-1, 1, num_stars), color='white', s=10)

# Rotate function
def update(frame):
    angle = y[frame]  # Get the angle from step response
    R = np.array([[np.cos(angle), -np.sin(angle), 0], 
                  [np.sin(angle), np.cos(angle), 0], 
                  [0, 0, 1]])  # Rotation matrix around Z-axis

    rotated = np.dot(R, np.vstack((body_x, body_y, body_z)))
    
    spacecraft.set_data(rotated[0, :], rotated[1, :])
    spacecraft.set_3d_properties(rotated[2, :])

    return spacecraft,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(t), blit=True, interval=20)

print("Saving to:", os.getcwd())
# Save as GIF
ani.save("spacecraft_rotation.gif", writer="pillow", fps=30)
# ani.save("spacecraft_rotation.mp4", writer="ffmpeg", fps=30) # OR save as MP4 (choose one)

# Set dark theme for space effect
ax.set_facecolor('black')
plt.show()


#-----------------------------Plotting for different Proportional gains----------------------------------------#

Kp_values = [1, 5, 10, 20]  # Different proportional gains

# Plot step response for different Kp values
plt.figure(figsize=(10, 6))

for Kp in Kp_values:
    G = ctl.tf([1], [I, 0, 0])  # Plant: 1/(I * s^2)
    T = ctl.feedback(Kp * G)  # Closed-loop system
    t, y = ctl.step_response(T, t)
    
    plt.plot(t, y, label=f"Kp={Kp}")

# Step Response Plot
plt.xlabel("Time (s)")
plt.ylabel("Angle θ (rad)")
plt.title("Step Response for Different Kp Values")
plt.legend()
plt.grid()
plt.savefig("step_response.png", dpi=300)  # 🔽 Save as PNG
plt.show()

# Bode Plot
plt.figure()
ctl.bode(T, dB=True)
plt.savefig("bode_plot.png", dpi=300)  # 🔽 Save Bode plot
plt.show()

# Nyquist Plot
plt.figure()
ctl.nyquist(T)
plt.savefig("nyquist_plot.png", dpi=300)  # 🔽 Save Nyquist plot
plt.show()

