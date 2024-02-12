import numpy as np

def read_equations(num_eq, equations):
    def F(x):
        f = np.zeros(num_eq)
        for i in range(num_eq):
            f[i] = eval(equations[i])
        return f

    def J(x):
        Jf = np.zeros((num_eq, num_eq))
        eps = 1e-6
        for i in range(num_eq):
            for j in range(num_eq):
                dx = np.zeros(num_eq)
                dx[j] = eps
                Jf[i, j] = (F(x + dx)[i] - F(x - dx)[i]) / (2 * eps)
        return Jf

    return F, J


def newton_raphson_system(F, J, x0, tol=1e-6, max_iter=100):
    x = np.array(x0)
    for i in range(max_iter):
        f = F(x)
        Jf = J(x)
        dx = np.linalg.solve(Jf, -f)
        x = x + dx
        if np.linalg.norm(dx) < tol:
            return x
    raise ValueError("The Newton-Raphson method did not converge.")


num_eq = int(input("Enter the number of equations: "))
equations = []
x0 = []
for i in range(num_eq):
    equations.append(input(f"Enter equation {i+1}: "))
    x0.append(float(input(f"Enter initial guess for x{i+1}: ")))
F, J = read_equations(num_eq, equations)
tol = float(input("Enter the tolerance: "))  #1e-6

#tol = 1e-6
x = newton_raphson_system(F, J, x0, tol=tol)
print("Roots found:", x)
#x[1] + 5*x[2] - 7*x[3] + 23*x[4] - x[5] + 7*x[6] + 8*x[7] + x[8] - 5*x[9] - 10
#17*x[0] - 24*x[2] - 75*x[3] + 100*x[4] - 18*x[5] + 10*x[6] - 8*x[7] + 9*x[8] - 50*x[9] + 40
#3*x[0] - 2*x[1] + 15*x[2] - 78*x[4] - 90*x[5] - 70*x[6] + 18*x[7] - 75*x[8] + x[9] + 17
#5*x[0] + 5*x[1] - 10*x[2] - 72*x[4] - x[5] + 80*x[6] - 3*x[7] + 10*x[8] - 18*x[9] - 43
#100*x[0] - 4*x[1] - 75*x[2] - 8*x[3] + 83*x[5] - 10*x[6] - 75*x[7] + 3*x[8] - 8*x[9] + 53
#70*x[0] + 85*x[1] - 4*x[2] - 9*x[3] + 2*x[4] + 3*x[6] - 17*x[7] - x[8] - 21*x[9] - 12
#x[0] + 15*x[1] + 100*x[2] - 4*x[3] - 23*x[4] + 13*x[5] + 7*x[7] - 3*x[8] + 17*x[9] + 60
#16*x[0] + 2*x[1] - 7*x[2] + 89*x[3] - 17*x[4] + 11*x[5] - 73*x[6] - 8*x[8] - 23*x[9] - 100
#51*x[0] + 47*x[1] - 3*x[2] + 5*x[3] - 10*x[4] + 18*x[5] - 99*x[6] - 18*x[7] + 12*x[9]
#x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] - 100

#Roots found: [ 87.49970902 -55.75380417  17.77411635  32.04744366  11.74397126 -94.36514182   9.18489557  -8.10628054  99.97509067  52.53605364]



