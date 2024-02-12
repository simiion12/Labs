

function [x, y] = xy(t)
  x = 3 .* sin(t);
  y = 2 .* cos(sin(t));
end

function ex_2_b(t1)
  t=0:4*pi;
  t1=4*pi*rand;
  pkg load symbolic
  syms t;
  [x,y]=xy(t);
  vx=diff(x);
  vy=diff(y);
  t=t1;
  vx1=eval(vx);
  vy1=eval(vy);

%Viteza
  v=sqrt(vx1^2+vy1^2);

%Acceleratia
  ax=diff(vx);
  ay=diff(vy);
  ax1=eval(ax);
  ay1=eval(ay);
  a=sqrt(ax1^2+ay1^2);

%Acceleratia tangentiala
  at=(ax1*vx1+ay1*vy1)/v;

%Acceleratia normala
  an=sqrt(a^2-at^2);

%Raza curburii traiectoriei
  r=v^2/an;

  atvc= at*[vx1, vy1]/v;
  anvc=an*[vx1, -vy1]/v;

  t=0:0.01:4*pi;
  [x,y]=xy(t);
  t=t1;
  [x1,y1]=xy(t);
  plot(x, y, x1, y1,'ro');
  hold on;

  quiver (x1, y1, vx1, vy1, 'r');
  quiver (x1, y1, ax1, ay1, 'k');
  quiver (x1, y1, atvc(1), atvc(2), 'y');
  quiver (x1, y1, anvc(1), anvc(2), 'm');
  axis equal tight;
  hold off;
  title ("Graficul traiectoriei a toţi vectorilor");
  legend('X(t) si Y(t)', 'Point', 'Viteza', 'Accel', 'AccelT', 'AccelN');

  fprintf(['Timpul = ', num2str(t1),' s | Viteza = ', num2str(v),' m/s | Acceleratia = ', num2str(a),'m/s^2 | Acceleratia tangentiala = ', num2str(at),' m/s^2 | Acceleratia normala = ', num2str(an),' m/s^2 | Raza = ', num2str(r),' m']);
end

% Exercise 2b
disp("Exercise 2b:");
t1 = 1.5*pi;
ex_2_b(t1);

