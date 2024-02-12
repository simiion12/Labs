function [x1,x2,x3]=fnecoer(t)
al=5;
a2=15;
omegal=15;
omega2=6;
alfal=pi/1.9;
alfa2=pi/1.2;
x1=al*sin(omegal*t+alfal);
x2=a2*sin(omega2*t+alfa2);
x3=x1+x2;
end

t=[0:pi/100:15];
[x1,x2,x3]=fnecoer(t);
figure(1);
plot(t,x1,':r',t,x2,'--b',t,x3,'-k');
legend('x1','x2','x1+x2');
title('compunerea oscilatiilor necoerente');
xlabel('t, sec');
ylabel('x, m');

function [x1,x2,x3]=fcoer(t)
al=5;
a2=15;
omegal=10;
omega2=10;
alfal=pi/9;
alfa2=pi/2;
x1=al*sin(omegal*t+alfal);
x2=a2*sin(omega2*t+alfa2);
x3=x1+x2;
end

t=0:pi/100:15;
[x1,x2,x3]=fcoer(t);
figure(2);
plot(t,x1,':r',t,x2,'--b',t,x3,'-k');
legend('x1','x2','x1+x2');
title('compunerea oscilatiilor coerente');
xlabel('t, sec');
ylabel('x, m');

function [x1,x2,x3] = fbataie(t, domega)
    al = 10;
    a2 = 12;
    omegal = 5;
    omega2 = omegal + domega;
    alfal = 1;
    alfa2 = 1;
    x1 = al*sin(omegal*t+alfal);
    x2 = a2*sin(omega2*t+alfa2);
    x3 = x1 + x2;
end

t = 0:pi/5:400;
n = 2;
for domega = [0.7, 0.15, 0.05]
    n = n+1;
    [x1, x2, x3] = fbataie(t, domega);
    figure(n);
    plot(t, x3, '-k', 'LineWidth', 1);
    axis equal
    legend('x1+x2');
    title(['oscilatie-bataie cu diferenta dintre pulsatie de ' num2str(domega) ' radiani']);
    xlabel('t, sec');
    ylabel('x, m');
end

function [x1,x2,x3] = falfa(t, dalfa)
    al = 10;
    a2 = 12;
    omegal = 5;
    omega2 = omegal + dalfa;
    alfal = pi/2;
    alfa2 = alfal + dalfa;
    x1 = al*sin(omegal*t+alfal);
    x2 = a2*sin(omega2*t+alfa2);
    x3 = x1 + x2;
end

t = 0:pi/200:10;
n = 0;
for alfa = [0, pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi]
    n = n+1;
    figure(6);
    subplot(3,3,n);
    [x1,x2,x3] = falfa(t, alfa);
    plot(t, x1, ':g', t, x2, '--b', t, x3, '-c', 'LineWidth', 1.0);
end

