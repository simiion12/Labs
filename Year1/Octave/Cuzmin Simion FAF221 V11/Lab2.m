
x1 = [pi:0.5:2*pi];
f1 = sin(x1) .^ 3;
g1 = cos(x1) .^ 3;


% Plot the functions with different colors and font sizes
figure(1);
plot(x1, f1, 'LineWidth', 2, 'Color', [1 0.5 0]);
xlabel('x','FontSize',18,'FontWeight','bold','Color',[0 0 1]);
ylabel('f(x)','FontSize',18,'FontWeight','bold','Color',[0 0 1]);

figure(2);
plot(x1, g1, 'LineWidth', 2, 'Color', [1 0.8 0]);
xlabel('x','FontSize',18,'FontWeight','bold','Color',[0 0 0.5]);
ylabel('g(x)','FontSize',18,'FontWeight','bold','Color',[0 0 0.5]);

% Plot both functions in the same plot with different line styles and font colors
figure(3);
plot(x1, f1, '-.', 'LineWidth', 2, 'Color', [1 0 0]);
hold on;
plot(x1, g1, '--', 'LineWidth', 2, 'Color', [0.5 0 0.5]);
xlabel('x','FontSize',18,'FontWeight','bold','Color',[0 0 0]);
ylabel('f(x) and g(x)','FontSize',18,'FontWeight','bold','Color',[0 0 0]);
legend('f(x)', 'g(x)','FontSize',14,'FontWeight','bold');

% Plot both functions in different subplots with different line styles and font sizes
figure(4);
subplot(3,1,1)
plot(x1, f1, '-', 'LineWidth', 2, 'Color', [0.5 0.5 0]);
xlabel('x','FontSize',14,'FontWeight','bold','Color',[0 0 0]);
ylabel('f(x)','FontSize',14,'FontWeight','bold','Color',[0 0 0]);

subplot(3,1,2)
plot(x1, g1, ':', 'LineWidth', 2, 'Color', [0 0.5 0.5]);
xlabel('x','FontSize',14,'FontWeight','bold','Color',[0 0 0]);
ylabel('g(x)','FontSize',14,'FontWeight','bold','Color',[0 0 0]);

subplot(3,1,3)
plot(x1, f1, '-.', 'LineWidth', 2, 'Color', [0.8 0.2 0.2]);
hold on;
plot(x1, g1, '--', 'LineWidth', 2, 'Color', [0.2 0.8 0.2]);
xlabel('x','FontSize',14,'FontWeight','bold','Color',[0 0 0]);
ylabel('f(x) and g(x)','FontSize',14,'FontWeight','bold','Color',[0 0 0]);
legend('f(x)', 'g(x)','FontSize',12);

figure(5);
subplot(1,3,1)
plot(x1, f1, 'LineWidth', 2, 'LineStyle', '--', 'Color', [0.5 0 0]);
xlabel('x','FontSize',18,'Color',[0.5 0 0]);
ylabel('f(x)','FontSize',18,'Color',[0.5 0 0]);
subplot(1,3,2)
plot(x1, g1, 'LineWidth', 2, 'LineStyle', ':', 'Color', [0.3 0 0]);
xlabel('x','FontSize',18,'Color',[0.3 0 0]);
ylabel('g(x)','FontSize',18,'Color',[0.3 0 0]);
subplot(1,3,3)
plot(x1, f1, 'LineWidth', 2, 'LineStyle', '-', 'Color', [0.1 0 0]);
hold on;
plot(x1, g1, 'LineWidth', 2, 'LineStyle', '--', 'Color', [0.1 0.5 0]);
xlabel('x','FontSize',18,'Color',[0.1 0 0]);
ylabel('f(x) and g(x)','FontSize',18,'Color',[0.1 0 0]);
legend('f(x)', 'g(x)');

figure(6);
subplot(2,2,1)
plot(x1, f1, 'LineWidth', 2, 'LineStyle', '-', 'Color', [0.5 0 0]);
xlabel('x','FontSize',18,'Color',[0.5 0 0]);
ylabel('f(x)','FontSize',18,'Color',[0.5 0 0]);
subplot(2,2,3)
plot(x1, g1, 'LineWidth', 2, 'LineStyle', ':', 'Color', [0.3 0 0]);
xlabel('x','FontSize',18,'Color',[0.3 0 0]);
ylabel('g(x)','FontSize',18,'Color',[0.3 0 0]);
subplot(2,2,[2 4])
plot(x1, f1, 'LineWidth', 2, 'LineStyle', '-', 'Color', [0.1 0 0]);
hold on;
plot(x1, g1, 'LineWidth', 2, 'LineStyle', '--', 'Color', [0 0.5 0]);
xlabel('x','FontSize',18,'Color',[0.1 0 0]);
ylabel('f(x) and g(x)','FontSize',18,'Color',[0.1 0 0]);
legend('f(x)', 'g(x)');

figure(7);
subplot(2,2,[1 2])
plot(x1, f1, 'LineWidth', 2, 'LineStyle', '-', 'Color', [0.5 0 0]);
xlabel('x','FontSize',18,'Color',[0.5 0 0]);
ylabel('f(x)','FontSize',18,'Color',[0.5 0 0]);
subplot(2,2,3)
plot(x1, g1, 'LineWidth', 2, 'LineStyle', ':', 'Color', [0.3 0 0]);
xlabel('x','FontSize',18,'Color',[0.3 0 0]);
ylabel('g(x)','FontSize',18,'Color',[0.3 0 0]);
subplot(2,2,4)
plot(x1, f1);
hold on;
plot(x1, g1);
xlabel('x','FontSize',18,'Color',[.1 0 0]);
ylabel('f(x) and g(x)','FontSize',18,'Color',[.1 0 0]);
legend('f(x)', 'g(x)');



x = [-1:0.2:2];
y = [-2:0.2:3];
[X, Y] = meshgrid(x, y);
z = exp(-abs(X)).*(X.^2+Y.^2).*cos(X.*Y);

figure(8);

subplot(2,3,1);
mesh(X, Y, z);
xlabel('x');
ylabel('y');
zlabel('z');
title('Mesh Plot');

subplot(2,3,2);
surf(X, Y, z);
xlabel('x');
ylabel('y');
zlabel('z');
title('Surface Plot');

subplot(2,3,3);
meshc(X, Y, z);
xlabel('x');
ylabel('y');
zlabel('z');
title('Mesh and Contour Plot');

subplot(2,3,4);
surfc(X, Y, z);
xlabel('x');
ylabel('y');
zlabel('z');
title('Surface and Contour Plot');

subplot(2,3,5);
contour(X, Y, z);
xlabel('x');
ylabel('y');
title('Contour Plot');

subplot(2,3,6);
contourf(X, Y, z);
xlabel('x');
ylabel('y');
colorbar;
title('Filled Contour Plot');

figure(9);
contour3(X, Y, z);
xlabel('x');
ylabel('y');
zlabel('z');
title('3D Contour Plot');
