# Projects 

First, a [simple project](BasicController.md) to get a hang of impleementing controllers then a few basic projects in areas of interest.

## Contents 

1.  [Autopilot System for an Aircraft (Pitch Control)](AircraftController.md)
  - Concepts Used: Transfer functions, PID control, stability analysis.
  - Description: Develop a pitch control system for an aircraft, designing a PID controller to maintain a desired pitch angle. You can use linearized aircraft dynamics (such as the short-period mode) and test different controller gains using root locus, Bode plots, and step response analysis.
  - Tools: Simulink (for simulation), Python (control library for analysis).

2. [Control of a Drone's Attitude](DroneController.md)
  - Concepts Used: Transfer function modeling, PID tuning, stability margins.
  - Description: Simulate the pitch/roll/yaw control of a quadcopter by implementing PID controllers for each axis. The system can be simplified as a second-order system and tested for step response, overshoot, and settling time.
  - Tools: Simulink (for simulation), Python (for tuning and stability analysis).

3. [Spacecraft Attitude Control using Reaction Wheels](SpacecraftController.md)
  - Concepts Used: State-space representation, nonlinear control.
  - Description: Model the Euler equations of motion for a spacecraft with reaction wheels, then design a state feedback controller to stabilize the orientation.
  - Tools: Simulink (for full dynamics simulation), Python (numpy, scipy.integrate for numerical solutions).

---
