% Definim parametrii sistemului mecanic
m = 1; % masa punctului material
k = 4; % constanta elasticitatii

% Definim functia de ecuatii diferentiale
f = @(t,x) [x(2); (-k/m)*x(1)];

% Definim conditiile initiale
x0 = [1; 0]; % pozitia initiala este 1, viteza initiala este 0

% Definim intervalul de timp
tspan = [0, 10];

% Rezolvam numeric ecuatia diferentiala
[t,x] = ode45(f, tspan, x0);

% Desenam graficul pozitiei in functie de timp
plot(t, x(:,1));
xlabel('Timp');
ylabel('Pozitie');
title('Oscilatii libere in lipsa rezistentei mediului');



function dxdt = eqn(x, r, k, m)
dxdt = [x(2); -(r/m)*x(2) - (k/m)*x(1)];
endfunction
#Putem apoi apela funcția ode45 pentru a obține soluția numerică:

m = 1; % masa punctului material
r = 0.5; % coeficientul de frecare
k = 2; % constanta elastică
x0 = [1; 0]; % condiții inițiale: poziția inițială și viteza inițială
tspan = [0, 10]; % intervalul de timp pentru care se rezolvă ecuația diferențială

[t, x] = ode45(@(t, x) eqn(x, r, k, m), tspan, x0);

#Graficul poziției în funcție de timp poate fi obținut astfel:
figure(2);
plot(t, x(:, 1));
xlabel('Timp');
ylabel('Pozitie');
title('Oscilatii libere in prezenta rezistentei mediului');




m = 1;      % masa punctului material
k = 1;      % constanta elastică a arcului
F = 2;      % amplitudinea forței oscilatorii
w = 1.5;    % pulsația oscilatorului

% definim ecuatia diferentiala
f = @(t,x) [x(2); (F*cos(w*t) - k*x(1))/m];

% setam conditiile initiale si intervalul de timp
tspan = [0 20];
x0 = [0 0];

% rezolvam ecuatia diferentiala
[t,x] = ode45(f, tspan, x0);

% afisam graficul pozitiei in functie de timp
figure(3);
plot(t, x(:,1));
xlabel('Timp');
ylabel('Pozitie');
title('Oscilatii fortate in lipsa rezistentei mediului');


m = 1;      % masa punctului material
k = 1;      % constanta elastică a arcului
b = 0.1;    % coeficientul de frecare
F = 2;      % amplitudinea forței oscilatorii
w = 1.5;    % pulsația oscilatorului

% definim ecuatia diferentiala
f = @(t,x) [x(2); (F*cos(w*t) - b*x(2) - k*x(1))/m];

% setam conditiile initiale si intervalul de timp
tspan = [0 20];
x0 = [0 0];

% rezolvam ecuatia diferentiala
[t,x] = ode45(f, tspan, x0);

% afisam graficul pozitiei in functie de timp
figure(4);
plot(t, x(:,1));
xlabel('Timp');
ylabel('Pozitie');
title('Oscilatii fortate in prezenta rezistentei mediului');

