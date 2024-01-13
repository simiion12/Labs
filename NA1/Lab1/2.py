def g(x, c):
    return 2 * x - c * x ** 2

def dg(x, c):
    return 2 - 2 * c * x

def fixed_point_iteration(c, x0, tol=1e-8, max_iter=100):
    def f(pn):
        return pn - g(pn, c)

    def df(pn):
        return 1 - dg(pn, c)

    for i in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise Exception("Fixed-point iteration failed to converge")

c = 5
x0 = 1

limit = fixed_point_iteration(c, x0)

print(f"The limit of g(x) = {c}x - {c}x^2 is: {limit}")

