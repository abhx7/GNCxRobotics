syms phi theta psi real

%ZYZ system
R1 = [cos(phi) -sin(phi) 0; sin(phi) cos(phi) 0; 0 0 1];
R2 = [cos(theta) 0 sin(theta); 0 1 0; -sin(theta) 0 cos(theta)];
R3 = [1 0 0; 0 cos(psi) -sin(psi); 0 sin(psi) cos(psi)];
simplify(R1*R2*R3);

simplify(subs(R1,phi,psi)*R2*R1)

