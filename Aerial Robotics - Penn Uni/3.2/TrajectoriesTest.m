% Define symbolic variable for time
syms t


%%%solution of x^(6) = 0

% Define the general 5th-degree polynomial for x(t)
% x(t) = a5*t^5 + a4*t^4 + a3*t^3 + a2*t^2 + a1*t + a0
x(t) = sym('a5')*t^5 + sym('a4')*t^4 + sym('a3')*t^3 + sym('a2')*t^2 + sym('a1')*t + sym('a0');

% Calculate velocity and acceleration by differentiating x(t)
v(t) = diff(x, t);  % First derivative of x(t)
a(t) = diff(v, t);  % Second derivative of x(t)

% Given boundary conditions
T = 5;          % Final time
x0 = 0;         % Initial position at t = 0
xT = 10;        % Final position at t = T
v0 = 0;         % Initial velocity at t = 0
vT = 0;         % Final velocity at t = T
a0 = 0;         % Initial acceleration at t = 0
aT = 0;         % Final acceleration at t = T

% Setup the system of equations for boundary conditions
eqns = [
    subs(x, t, 0) == x0,   % x(0) = x0
    subs(x, t, T) == xT,   % x(T) = xT
    subs(v, t, 0) == v0,   % v(0) = v0
    subs(v, t, T) == vT,   % v(T) = vT
    subs(a, t, 0) == a0,   % a(0) = a0
    subs(a, t, T) == aT    % a(T) = aT
];

% Solve for the coefficients of the polynomial
coeffs = solve(eqns, {'a5', 'a4', 'a3', 'a2', 'a1', 'a0'});

% Substitute the coefficients into the expressions for x(t), v(t), and a(t)
% Convert symbolic expressions to MATLAB functions for numerical evaluation
x_func = matlabFunction(subs(x, coeffs));
v_func = matlabFunction(subs(v, coeffs));
a_func = matlabFunction(subs(a, coeffs));

% Time vector for plotting
t_vals = linspace(0, T, 100);

% Evaluate position, velocity, and acceleration over time
x_vals = x_func(t_vals);
v_vals = v_func(t_vals);
a_vals = a_func(t_vals);

% Plotting the results
figure;
subplot(3,1,1);
plot(t_vals, x_vals, 'r', 'LineWidth', 2);
%xlabel('Time t');
ylabel('Position x(t)');
title('Position vs Time');
grid on;

subplot(3,1,2);
plot(t_vals, v_vals, 'g', 'LineWidth', 2);
%xlabel('Time t');
ylabel('Velocity v(t)');
title('Velocity vs Time');
grid on;

subplot(3,1,3);
plot(t_vals, a_vals, 'b', 'LineWidth', 2);
xlabel('Time t');
ylabel('Acceleration a(t)');
title('Acceleration vs Time');
grid on;


% Lagrange function (minimizing square of third derivative of x(t))
%L = diff(x, t, 3)^2;

% Euler-Lagrange equation for minimizing the Lagrange function
%EL_eqn = functionalDerivative(L, x);

% Given boundary conditions

% Solve the differential equation symbolically with boundary conditions
%xSol(t) = dsolve(EL_eqn, x(0) == x0, x(T) == xT, ...
 %   diff(x, t) == v0, subs(diff(x, t), t, T) == vT, ...
  %  diff(x, t, 2) == a0, subs(diff(x, t, 2), t, T) == aT);

% Derive velocity and acceleration from the solution
%vSol(t) = diff(xSol, t);   % Velocity is the first derivative of xSol
%aSol(t) = diff(vSol, t);   % Acceleration is the second derivative of xSol
