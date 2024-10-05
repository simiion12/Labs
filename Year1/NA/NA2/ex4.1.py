import scipy.integrate as spi
import scipy.special
import math

def f(x, t):
    return math.pow(t, x - 1) * math.exp(-t)

def Gamma(x):
    return scipy.special.gamma(x)

a = 0
b = 1
n = 3

while Gamma(b) - Gamma(a) < 0.00000001:
    a += 1
    b += 1
    n += 1

if n % 2 == 0:
    n += 1

def composite_Simpson(Gamma, a, b, n):
    if n % 2 == 0:
        return None

    h = (b - a) / n
    first = Gamma(a)
    last = Gamma(b)

    x = a
    sum = 0
    for i in range(1, n):
        x += h
        value = Gamma(x)
        if i % 2 == 0:
            sum += 2 * value
        else:
            sum += 4 * value
    total = (h / 3) * (first + sum + last)
    return total

print(composite_Simpson(Gamma, 1, 10, 7))
print(spi.quad(Gamma, 1, 10, epsabs=0.00000001))


