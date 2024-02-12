pkg load symbolic

function y=funct(t)
  y=9.2*sin(3*pi*t)^2-(195*pi/180);
endfunction

t1=fzero(@funct,pi/2);

syms t;
fi=9.2*sin(3*pi*t)^2;
w=diff(fi);
w1=subs(w,t,t1);
w1=eval(w1);  %viteza unghiulara placii

function [feta]=phi1(t)
  feta=9.2*sin(3*pi*t)^2;
endfunction

R=40;
phi=phi1(t1);

%Coordonatele punctului la momentul de timp t
x=R*cos(phi);
y=R*sin(phi);

e=diff(w);
e1=subs(e,t,t1);
e1=eval(e1);  %acceleratia placii

v=w1*R;  %viteza punctului
a_ax=w1^2*R ; %acceleratia normala a punctului
a_rot=e1*R;  %acceleratia tangentiala a punctului
a=sqrt(a_ax^2+a_rot^2);

disp(["t = ", num2str(t1)," s";
      "x = ", num2str(x)," m";
      "y = ", num2str(y)," m";
      "w = ", num2str(w1)," rad/s";
      "e = ", num2str(e1)," rad/s2";
      "v = ", num2str(v)," m/s";
      "a_ax = ", num2str(a_ax)," m/s2";
      "a_rot = ", num2str(a_rot)," m/s2"
      "a = ", num2str(a)," m/s2";])

