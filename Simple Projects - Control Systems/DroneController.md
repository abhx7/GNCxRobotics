# **Project 2: Drone Attitude Control (PID)**  

🏗️ **Objective:**  
Develop a **PID controller** to stabilize and control a drone’s **pitch, roll, and yaw**. Each axis will be modeled as a **second-order system**, and a PID controller will be tuned for stability.  

---

## **Step 1: Dynamics of a Single Axis (Roll/Pitch/Yaw)**  
For a simplified drone model, each axis behaves like a **second-order system**:  

![Equation](https://quicklatex.com/cache3/b1/ql_fd3374aa05e9fb1f21fcdbc67f110db1_l3.png)

The transfer function representation:  

![Equation](https://quicklatex.com/cache3/ee/ql_1affa5a62e829b5bf822e3015ed8daee_l3.png)

where:  
- Θ(s) = Angular position (roll, pitch, or yaw)  
- M(s) = Control torque applied by drone motors  
- J = Moment of inertia  
- b = Aerodynamic damping  

For a single axis, the system can be approximated as a **second-order transfer function**:  

![Equation](https://quicklatex.com/cache3/73/ql_488533965c3da44f7aa58bf551450f73_l3.png)

---

## **Step 2: Implement in Simulink/Python**  
- **Simulink:** Use a **second-order system block** and apply a **PID controller block**.  
- **Python:** Use `control.TransferFunction()` to model the system and `control.step_response()` to visualize the response.  

---

## **Step 3: PID Controller Design**  

### **Manual Tuning Approach**  
- **Proportional Gain (Kₚ)**: Increases speed but may introduce overshoot.  
- **Integral Gain (Kᵢ)**: Reduces steady-state error but may cause oscillations.  
- **Derivative Gain (Kd)**: Reduces overshoot and stabilizes.  

#### **Tuning method:**  
1. Start with only Kₚ to get an initial response.  
2. Add Kd to reduce overshoot.  
3. Introduce Kᵢ to remove steady-state error.  

---

### **Auto-Tuning Using Ziegler-Nichols**  
1. Set Kᵢ = 0, Kd= 0 .  
2. Increase Kₚ until the system **oscillates**.  
3. Use oscillation period Tᵤ to calculate optimal PID gains:  

![Equation](https://quicklatex.com/cache3/58/ql_ebccc033bcc61d4f7725ff23c29baf58_l3.png)
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
