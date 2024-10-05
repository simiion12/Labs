import math

def bisection_method(f, a, b, tol, max_iter):
    if f(a) * f(b) > 0:
        print("Error: f(a) and f(b) do not have opposite signs.")
        return None

    n_iter = 0

    while n_iter < max_iter:
        c = (a + b) / 2.0

        if abs(f(c)) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        n_iter += 1

def f(x):
    return math.exp(x) - x ** 2

# Find a root of f(x) on the interval [-2, 0]
root = bisection_method(f, -2, 0, tol=1e-8, max_iter=1000)

print("A root of the equation e^x - x**2 = 0 is", root)
