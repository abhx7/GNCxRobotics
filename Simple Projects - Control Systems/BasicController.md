# **Project: Single-Axis Attitude Control Using a Proportional Controller**

## **Objective:**  
Control the **angular position** of a spacecraft/drone along a single axis (e.g., pitch).  

---

## **Step 1: System Dynamics (Single-Axis Rotation)**  
The rotational dynamics can be approximated as:

![Equation](https://quicklatex.com/cache3/d8/ql_b2299087ca63642a93e8ad7b3f59acd8_l3.png)


where:  
- I  = Moment of inertia about the axis  
- θ = Angular position  
- M  = Control torque applied  

Taking the **Laplace transform**:  

![Equation](https://quicklatex.com/cache3/3f/ql_94ecbde34f065dd8e45fbfbb276a2d3f_l3.png)

Assuming initial conditions are zero,

![Equation](https://quicklatex.com/cache3/66/ql_511bf8f0c921630b16c4939c9bcf6566_l3.png)

The **open-loop transfer function** is:

![Equation](https://quicklatex.com/cache3/51/ql_466f397dcf6761de153201f098199d51_l3.png)

![Image](https://github.com/abhx7/Control-Systems/blob/main/Simple%20Projects%20-%20Control%20Systems/BasicController-OpenLoopBD.png)

This is a **double integrator system**, meaning **without control, the angular position will keep changing indefinitely**.  

---

## **Step 2: Proportional Control Design**  
A proportional controller applies torque based on the angular position error:

![Equation](https://quicklatex.com/cache3/ed/ql_92ef34dac90e5c774e599b60ddfb67ed_l3.png)

In Laplace form:

![Equation](https://quicklatex.com/cache3/33/ql_e8f86c9ddeea56e236290312906ab933_l3.png)

Using **unity feedback**, the **closed-loop transfer function** is:

![Equation](https://quicklatex.com/cache3/4d/ql_eafb61a1ad97634c1346066d1aee404d_l3.png)

![Image](https://github.com/abhx7/Control-Systems/blob/main/Simple%20Projects%20-%20Control%20Systems/BasicController-ClosedLoopBD.png)

Since this is still a **second-order system**, the response depends on **![Equation](https://quicklatex.com/cache3/97/ql_472657be04f1eaed46d63aa1534c2397_l3.png)**:  
- **Higher ![Equation](https://quicklatex.com/cache3/97/ql_472657be04f1eaed46d63aa1534c2397_l3.png)** → Faster response but **higher oscillations**.  
- **Lower ![Equation](https://quicklatex.com/cache3/97/ql_472657be04f1eaed46d63aa1534c2397_l3.png)** → Slower response with **minimal oscillations**.  

---

## **Step 3: Simulink & Python Basic Implementation**   

### **Simulink Setup:**  
1. Create a **second-order system block**:  

   ![Equation](https://quicklatex.com/cache3/c7/ql_ca82c0e253f56da8ce1a3598db68a7c7_l3.png)

2. Add a **gain block** for ![Equation](https://quicklatex.com/cache3/97/ql_472657be04f1eaed46d63aa1534c2397_l3.png).  
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
✔ **If** ![Equation](https://quicklatex.com/cache3/97/ql_472657be04f1eaed46d63aa1534c2397_l3.png) **is small** → The response is **slow and steady**.  
✔ **If** ![Equation](https://quicklatex.com/cache3/97/ql_472657be04f1eaed46d63aa1534c2397_l3.png) **is large** → The response is **faster but may overshoot**.  
✔ **Without** ![Equation](https://quicklatex.com/cache3/4a/ql_16700456c6d1465a43e0426f2e9bc54a_l3.png) (derivative control), the system **may oscillate and never fully settle**.  

---

## Detailed Analysis 
From the code, 


---
## Possible Extensions
✅ **Implement friction/damping** ![Equation](https://quicklatex.com/cache3/76/ql_a0619f4555f93c31dd585aa1c54b3c76_l3.png) in the dynamics.  
✅ **Test step response, disturbance rejection** (simulate external torque).  
✅ **Compare proportional control with PID** for better performance.  


