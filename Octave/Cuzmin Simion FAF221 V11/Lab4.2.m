function [x1,x2]=fperp(t,alfa)
al=5;
a2=15;
omegal=10;
omega2=10;
alfal=alfa;
alfa2=0;
x1=al*sin(omegal*t+alfal);
x2=a2*cos(omega2*t+alfa2);
end

t=0:0.1:5;
n=0;
figure(1);
for alfa=[0, pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi]
    n=n+1;
    subplot(3, 3, n);
    [x1,x2]=fperp(t,alfa);
    plot(x1, x2, 'LineWidth', 1.5);
    title({alfa});
    xlabel('t,sec');
    ylabel('x,m');

end

function [x1,x2]=fperp2(t,alfa)
al=5;
a2=15;
omegal=2*pi/7;
omega2=3*pi/7;
#alfal=alfa;
#alfa2=0;
x1=al*sin(omegal*t-alfa-pi/2);
x2=a2*cos(omega2*t-alfa-pi/2);
end

t=0:0.1:100;
n=0;
figure(2);
for alfa=[0, pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi]
    n=n+1;
    subplot(3,3,n);
    [x1,x2]=fperp2(t,alfa);
    plot(x1,x2,'--','LineWidth',1.5);
    title(sprintf('\\alpha = %.2f', alfa));
    xlabel('x_1, m');
    ylabel('x_2, m');

end


