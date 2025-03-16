# **Project 1: Spacecraft Attitude Control using Reaction Wheels**

🚀 **Objective:**  
Design a **state feedback controller** to stabilize and control the attitude (orientation) of a spacecraft using **reaction wheels**. This will involve modeling the **Euler equations of motion**, implementing **state-space representation**, and designing a controller to regulate the spacecraft's angular velocity.

---

## **Step 1: Mathematical Modeling**
A spacecraft’s rotational motion is governed by **Euler’s equations**:

\[
I \dot{\omega} + \omega \times (I \omega) = M
\]

where:  
- \( I \) = **Moment of inertia matrix** (assumed diagonal for simplicity: \( I_x, I_y, I_z \))  
- \( \omega = [\omega_x, \omega_y, \omega_z] \) = Angular velocity vector  
- \( M = [M_x, M_y, M_z] \) = External torques from reaction wheels  

For small-angle approximations, the system can be linearized as:

\[
\dot{\omega} = I^{-1} (M - \omega \times (I \omega))
\]

In state-space form:

\[
\begin{bmatrix} \dot{\omega_x} \\ \dot{\omega_y} \\ \dot{\omega_z} \end{bmatrix} =
\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}
\begin{bmatrix} \omega_x \\ \omega_y \\ \omega_z \end{bmatrix} +
\begin{bmatrix} 1/I_x & 0 & 0 \\ 0 & 1/I_y & 0 \\ 0 & 0 & 1/I_z \end{bmatrix}
\begin{bmatrix} M_x \\ M_y \\ M_z \end{bmatrix}
\]

---

## **Step 2: Implement in Simulink/Python**
- **Simulink:** Create a state-space block for the dynamics, input the control torques from reaction wheels, and visualize the response.
- **Python:** Use `scipy.integrate.solve_ivp()` for numerical integration and `matplotlib` to plot orientation over time.

---

## **Step 3: Controller Design**
### **Proportional-Derivative (PD) Controller:**
Control torque:

\[
M = -K_p (\theta - \theta_{ref}) - K_d \omega
\]

- Simulate in Simulink/Python and tune **\( K_p \) and \( K_d \)** for stable attitude control.
  
### **State Feedback Control (LQR)**
Define a cost function:

\[
J = \int (\omega^T Q \omega + M^T R M) dt
\]

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
