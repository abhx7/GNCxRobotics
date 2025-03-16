# **Project 2: Drone Attitude Control (PID)**  

🏗️ **Objective:**  
Develop a **PID controller** to stabilize and control a drone’s **pitch, roll, and yaw**. Each axis will be modeled as a **second-order system**, and a PID controller will be tuned for stability.  

---

## **Step 1: Dynamics of a Single Axis (Roll/Pitch/Yaw)**  
For a simplified drone model, each axis behaves like a **second-order system**:  

\[
I \ddot{\theta} = M
\]

The transfer function representation:  

\[
\frac{\Theta(s)}{M(s)} = \frac{K}{Js^2 + bs}
\]

where:  
- \( \Theta(s) \) = Angular position (roll, pitch, or yaw)  
- \( M(s) \) = Control torque applied by drone motors  
- \( J \) = Moment of inertia  
- \( b \) = Aerodynamic damping  

For a single axis, the system can be approximated as a **second-order transfer function**:  

\[
G(s) = \frac{K}{s^2 + 2\zeta\omega_n s + \omega_n^2}
\]

---

## **Step 2: Implement in Simulink/Python**  
- **Simulink:** Use a **second-order system block** and apply a **PID controller block**.  
- **Python:** Use `control.TransferFunction()` to model the system and `control.step_response()` to visualize the response.  

---

## **Step 3: PID Controller Design**  

### **Manual Tuning Approach**  
- **Proportional Gain \( K_p \)**: Increases speed but may introduce overshoot.  
- **Integral Gain \( K_i \)**: Reduces steady-state error but may cause oscillations.  
- **Derivative Gain \( K_d \)**: Reduces overshoot and stabilizes.  

#### **Tuning method:**  
1. Start with only \( K_p \) to get an initial response.  
2. Add \( K_d \) to reduce overshoot.  
3. Introduce \( K_i \) to remove steady-state error.  

---

### **Auto-Tuning Using Ziegler-Nichols**  
1. Set \( K_i = 0, K_d = 0 \).  
2. Increase \( K_p \) until the system **oscillates**.  
3. Use oscillation period \( T_u \) to calculate optimal PID gains:  

\[
K_p = 0.6 K_u, \quad K_i = 1.2 K_u / T_u, \quad K_d = 3 K_u T_u / 40
\]

---

## **Step 4: Performance Evaluation**  
✔ **Step Response Analysis:** Check rise time, overshoot, and settling time.  
✔ **Bode Plot Stability Analysis:** Verify gain and phase margins.  
✔ **Disturbance Rejection:** Introduce **wind disturbances** and check stability.  

---

## **Possible Extensions**  
🔹 Implement **nonlinear model** including motor dynamics.  
🔹 Introduce **sensor noise** (simulate IMU errors).  
🔹 Design an **adaptive PID controller** (self-tuning PID).  
