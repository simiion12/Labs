clear
pkg load symbolic


coef=[1,1.5,0.75,-195*pi/180];
r=roots(coef);
for i=1:3
  if isreal(r(i))
    t1=r(i)
  endif
endfor


syms t;
fi=t^3+3*t^2+t;
w=diff(fi);
w1=subs(w,t,t1);
w1=eval(w1);  %viteza unghiulara placii

function [feta]=phi(t)
  feta=t^3+3*t^2+t;
 endfunction
R=40;
phi=phi(t1);
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
      "e = ", num2str(e1)," rad/s";
      "v = ", num2str(v)," rad/s";
      "a_ax = ", num2str(a_ax)," rad/s2";
      "a_rot = ", num2str(a_rot)," rad/s2"
      "a = ", num2str(a)," rad/s2";])

