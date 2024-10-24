
def hybrid_secant_bisection(f, a, b, tol, max_iter):
    iter_count = 0
    x0 = a
    x1 = b
    while iter_count < max_iter:
        f0 = f(x0)
        f1 = f(x1)
        f_diff = f1 - f0
        x_diff = x1 - x0
        if f_diff == 0:
            return x1
        df_dx1 = f_diff / x_diff
        x_next = x1 - f1 / df_dx1
        if x_next < a or x_next > b:
            x_next = (a + b) / 2
        if abs(f(x_next)) < tol:
            return x_next
        x0 = x1
        x1 = x_next
        iter_count += 1
    return x1

def f(x):
    import math
    return eval(equation)

equation = input(f"Enter equation : ")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

root = hybrid_secant_bisection(f, a, b, 1e-6, 1000)
print(root)

#3*x**6 + 5*math.exp(x) - 2*math.sin(x) - 6*x**2 - 10
#[-1,1]

# 2*x**6 - 7*x**5 - 8*x**4 + 23*x**3 + 25*x**2 - 31*x + 10
#[1,3]