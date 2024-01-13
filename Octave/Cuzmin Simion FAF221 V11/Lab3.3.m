pkg load symbolic
clf
tmax = 4*pi;
pas = 0.05;
t = 0:pas:tmax;

x = t.*(1-cos(2.*t));
y = t.*(sin(2.*t));
z = 1.3.*t;

figure(1)
%Construim traiectoria
%punctului material
comet3(x, y, z);
plot3(x, y, z);
hold on

%Determinam timpul de
%calcul si pozitia punctului
t1 = tmax*rand;
x1 = t1.*(1-cos(2.*t1));
y1 = t1.*(sin(2.*t1));
z1 = 1.3.*t1;

%Construim pozitia punctului
plot3(x1, y1, z1, 'ro-');
title(['t = ', num2str(t1)]);
hold on;
grid on;
xlabel('axa-OX');
ylabel('axa-OY');
zlabel('axa-OZ');
legend('Traiectoria');
grid minor;

%viteza
syms t2
x2 = t2.*(1-cos(2.*t2));
y2 = t2.*(sin(2.*t2));
z2 = 1.3.*t2;
vx = diff(x2);
vy = diff(y2);
vz = diff(z2);
t1_val = t1;
vx1 = subs(vx, t2, t1_val);
vy1 = subs(vy, t2, t1_val);
vz1 = subs(vy, t2, t1_val);
vx1 = eval(vx1);
vy1 = eval(vy1);
vz1 = eval(vz1);
v = sqrt(vx^2+vy^2+vz^2);
v1 = sqrt(vx1^2+vy1^2+vz1^2);

%Acceleratia
ax = diff(vx);
ay = diff(vy);
az = diff(vz);
ax1 = subs(ax, t2, t1_val);
ay1 = subs(ay, t2, t1_val);
az1 = subs(az, t2, t1_val);
ax1 = eval(ax1);
ay1 = eval(ay1);
az1 = eval(az1);
a1 = sqrt(ax1^2+ay1^2+az1^2);

%Acceleratia tangentiala
at = diff(v);
at1 = subs(at, t2, t1_val);
at1 = eval(at1);

%Acceleratia normala
an1 = sqrt(a1^2-at1^2);

%Raza curburii
r = v1^2/an1;

disp(["t = ", num2str(t1), " s";
      "x = ", num2str(x1), " m";
      "y = ", num2str(y1), " m";
      "z = ", num2str(z1), " m";
      "v = ", num2str(v1), " m/s";
      "a = ", num2str(a1), " m/s2";
      "at = ", num2str(at1), " m/s2";
      "an = ", num2str(an1), " m/s2";
      "r = ", num2str(r), " m"])

