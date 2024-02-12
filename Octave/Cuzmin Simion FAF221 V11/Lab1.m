% Lucrare de laborator Nr.1
% Student Cuzmin Simion FAF-221
% Varianta 11

% Sarcina II.1. Calcularea expresiilor intr-un rand
x = -1.75e-3
y = 3.1*pi
B1 = ((x^3 + tan(y)) / (sin(y) - log(abs(x)))^2.3 + (sin(y) - log(abs(x))) * 2.5 / sqrt(x^3 + tan(y)) + abs(x * sin(y)^2))
Q2 = ((x^3 - cos(y))^1.3 / (abs(x) + abs(sin(y))) + x^2 * (abs(x) + abs(sin(y)))^1.3 / (x^3 - cos(y))^(1/3))
disp("B1 (default):");
disp(B1);
disp("Q2 (default):");
disp(Q2);

format hex;
disp("B1 (hex):");
disp(B1);
disp("Q2 (hex):");
disp(Q2);

format bank;
disp("B1 (bank):");
disp(B1);
disp("Q2 (bank):");
disp(Q2);

format rat;
disp("B1 (rat):");
disp(B1);
disp("Q2 (rat):");
disp(Q2);
a = (x^3 + tan(y)) / (sin(y) - log(abs(x)));
b = sin(y) - log(abs(x));
c = sqrt(x^3 + tan(y));
d = abs(x * sin(y)^2);
e = x^3 - cos(y);
f = abs(x) + abs(sin(y));
g = abs(x) + abs(sin(y));
h = (x^3 - cos(y))^(1/3);
disp('cu variabile intermediare:');
F11 = (a)^2.3 + b*2.5/c + d;
F22 = e^1.3/f + x^2*f^1.3/h;
disp('a=')
disp(a)
disp('b=')
disp(b)
disp('c=');
disp(c)
disp('d=');
disp(d)
disp('e=');
disp(e)
disp('f=');
disp(f)
disp('h=');
disp(h)
disp('F11=');
disp(F11)
disp('F22=');
disp(F22)
whos B1 Q2 a b c e f h F11 F22



a = -pi/2;
b = 3*pi/2;
N = 6;
pas = (b-a)/(N-1);
x = [a:pas:b]
y = (sin(x) .* log(abs(x).^3 + 2) + x.^2 .* cos(x));
disp("The values of x are:")
disp(x);
disp("The values of y(x) are:")
disp(y);


