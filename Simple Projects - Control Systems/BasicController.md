# **Project: Single-Axis Attitude Control Using a Proportional Controller**

## **Objective:**  
Control the **angular position** of a spacecraft/drone along a single axis (e.g., pitch).  

---

## **Step 1: System Dynamics (Single-Axis Rotation)**  
The rotational dynamics can be approximated as:

![Equation](https://latex.codecogs.com/svg.latex?\Large%20I\ddot{\theta}=M)


where:  
- \( I \) = Moment of inertia about the axis  
- \( \theta \) = Angular position  
- \( M \) = Control torque applied  

Taking the **Laplace transform** (assuming initial conditions are zero):  

\[
I s^2 \Theta(s) = M(s)
\]

The **open-loop transfer function** is:

\[
G(s) = \frac{\Theta(s)}{M(s)} = \frac{1}{I s^2}
\]

This is a **double integrator system**, meaning **without control, the angular position will keep changing indefinitely**.  

---

## **Step 2: Proportional Control Design**  
A proportional controller applies torque based on the angular position error:

\[
M = -K_p (\theta - \theta_{ref})
\]

In Laplace form:

\[
M(s) = -K_p (\Theta(s) - \Theta_{ref}(s))
\]

Using **unity feedback**, the **closed-loop transfer function** is:

\[
T(s) = \frac{K_p}{I s^2 + K_p}
\]

Since this is still a **second-order system**, the response depends on **\( K_p \)**:  
- **Higher \( K_p \)** → Faster response but **higher oscillations**.  
- **Lower \( K_p \)** → Slower response with **minimal oscillations**.  

---

## **Step 3: Simulink & Python Implementation**  

### **Simulink Setup:**  
1. Create a **second-order system block**:  

   \[
   G(s) = \frac{1}{I s^2}
   \]

2. Add a **gain block** for \( K_p \).  
3. Connect a **step input** (desired angle) and observe the output.  

---

### **Python Code (Using `control` Library)**  

```python
import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Define system parameters
I = 5  # Moment of inertia
Kp = 10  # Proportional gain

# Transfer function: 1 / (I * s^2)
G = ctl.tf([1], [I, 0, 0])

# Closed-loop system with proportional control
T = ctl.feedback(Kp * G)

# Time vector
t = np.linspace(0, 10, 1000)

# Step response
t, y = ctl.step_response(T, t)

# Plot results
plt.plot(t, y, label=f"Kp={Kp}")
plt.xlabel("Time (s)")
plt.ylabel("Angle θ (rad)")
plt.title("Proportional Control Response")
plt.legend()
plt.grid()
plt.show()
```

## Step 4: Observations & Tuning
✔ **If** \( K_p \) **is small** → The response is **slow and steady**.  
✔ **If** \( K_p \) **is large** → The response is **faster but may overshoot**.  
✔ **Without** \( K_d \) (derivative control), the system **may oscillate and never fully settle**.  

---

## Possible Extensions
✅ **Implement friction/damping** \( b \dot{\theta} \) in the dynamics.  
✅ **Test step response, disturbance rejection** (simulate external torque).  
✅ **Compare proportional control with PID** for better performance.  


<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
