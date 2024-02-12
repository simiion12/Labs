import numpy as np

# Gauss-Legendre (default interval is [-1, 1])
def gauss_legendre(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def gauss_legendre_quad(f, a, b, n, tol):
    # Change of interval
    x, w = gauss_legendre(n)
    t = 0.5*(x + 1)*(b - a) + a
    gauss_quad = sum(w * f(t)) * 0.5 * (b - a)

    # Check the error estimate
    x1, w1 = gauss_legendre(2*n)
    t1 = 0.5*(x1 + 1)*(b - a) + a
    gauss_quad1 = sum(w1 * f(t1)) * 0.5 * (b - a)

    if abs(gauss_quad1 - gauss_quad) < tol:
        return gauss_quad
    else:
        return gauss_legendre_quad(f, a, b, 2*n, tol)

# Test

# Provide the function as input
f_input = input("Please enter your function of x: ")    # 3*x**5 + 2*x**4 - 7*x**3 + 6*x**2 - 4*x + 1
f = lambda x: eval(f_input)
f = np.vectorize(f)

# Interval [a, b]
a = float(input("Enter the start of the interval (a): "))   #0
b = float(input("Enter the end of the interval (b): "))    #1

# Tolerance
tol = float(input("Enter the tolerance: "))  #1e-6

# Initial number of points
n = int(input("Enter the initial number of points: "))   #10

print("The approximate value of the integral is:", gauss_legendre_quad(f, a, b, n, tol))