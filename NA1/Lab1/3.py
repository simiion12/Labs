import math
def muller(f, x0, x1, x2, tol=1e-8, max_iter=100):
    for i in range(max_iter):
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f(x1) - f(x0)) / h0
        d1 = (f(x2) - f(x1)) / h1
        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = f(x2)
        disc = math.sqrt(b ** 2 - 4 * a * c)
        if abs(b - disc) > abs(b + disc):
            den = b - disc
        else:
            den = b + disc
        dx = -2 * c / den
        x3 = x2 + dx
        if abs(dx) < tol:
            return x3
        x0 = x1
        x1 = x2
        x2 = x3
    raise Exception("Muller's method failed to converge")

def f(x):
    return x ** 3 + 2 * x ** 2 + 10 * x - 20

x0 = 0
x1 = 1
x2 = 2
tol = 1e-8

root = muller(f, x0, x1, x2, tol)

print("A root of the equation x^3 + 2x^2 + 10x - 20 = 0 is:")
print(f"{root:.8f}")
