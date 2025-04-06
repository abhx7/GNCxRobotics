# **Project 1: Spacecraft Attitude Control using Reaction Wheels**

🚀 **Objective:**  
Design a **state feedback controller** to stabilize and control the attitude (orientation) of a spacecraft using **reaction wheels**. This will involve modeling the **Euler equations of motion**, implementing **state-space representation**, and designing a controller to regulate the spacecraft's angular velocity.

---

## **Step 1: Mathematical Modeling**
A spacecraft’s rotational motion is governed by **Euler’s equations**:

![Equation](https://quicklatex.com/cache3/bc/ql_5ef3dfc992d1aa916d5fda1c32fc33bc_l3.png)

where:  
- I  = **Moment of inertia matrix** (assumed diagonal for simplicity: Iₓ, Iy, Iz)  
- ω = [ωₓ, ωy, ωz] = Angular velocity vector  
- M = [Mₓ, My, Mz] = External torques from reaction wheels  

For small-angle approximations, the system can be linearized as:

![Equation](https://quicklatex.com/cache3/ff/ql_edf48c25cfe431b779c38df42d5fadff_l3.png)

In state-space form:

![Equation](https://quicklatex.com/cache3/54/ql_bc0c7393d0f50d694a4630618d506254_l3.png)
---

## **Step 2: Implement in Simulink/Python**
- **Simulink:** Create a state-space block for the dynamics, input the control torques from reaction wheels, and visualize the response.
- **Python:** Use `scipy.integrate.solve_ivp()` for numerical integration and `matplotlib` to plot orientation over time.

---

## **Step 3: Controller Design**
### **Proportional-Derivative (PD) Controller:**
Control torque:

![Equation](https://quicklatex.com/cache3/55/ql_41b813cbed9fec79be7b32b55a2a8e55_l3.png)

- Simulate in Simulink/Python and tune **Kp and Kd** for stable attitude control.
  
### **State Feedback Control (LQR)**
Define a cost function:

![Equation](https://quicklatex.com/cache3/d2/ql_b09d02827b08d27d28610b6a93a6ecd2_l3.png)

- Use `control.lqr()` in Python to get **optimal feedback gains**.

---

## **Step 4: Performance Analysis**
- **Stability Check:** Verify eigenvalues of the closed-loop system.  
- **Time Response Analysis:** Step response, settling time, and overshoot.  
- **Disturbance Rejection:** Apply small external disturbances and check system response.

---

## **Possible Extensions**
🔹 Implement quaternion-based control (for **nonlinear dynamics**)  
🔹 Add **actuator saturation limits** (reaction wheels have limited torque)  
🔹 Introduce **external disturbances** (gravity gradient, aerodynamic drag)
