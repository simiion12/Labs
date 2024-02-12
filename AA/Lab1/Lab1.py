import time
import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable


test_for_recursive = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
test_for_other = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

result = {'fibonacci_recursive': [0.0, 0.0, 0.0, 8.320808410644531e-05, 0.0, 0.0, 0.0021009445190429688, 0.005815744400024414, 0.02409076690673828, 0.05990433692932129, 0.25200343132019043, 0.5971388816833496, 2.5020530223846436, 6.337579965591431, 26.376286268234253, 62.44957232475281, 273.80995440483093],
          'fibonacci_matrix': [5.909998435527086e-05, 4.1700026486068964e-05, 4.050001734867692e-05, 4.710000939667225e-05, 0.00020599999697878957, 6.470002699643373e-05, 6.079999729990959e-05, 8.620001608505845e-05, 8.890003664419055e-05, 0.00010939995991066098, 0.0001401000190526247, 0.0002049999893642962, 0.00027600000612437725, 0.00036750000435858965, 0.000499500019941479, 0.0007117000059224665],
          'fibonacci_binet': [9.800016414374113e-06, 3.7999707274138927e-06, 3.600027412176132e-06, 2.3999600671231747e-06, 2.500019036233425e-06, 2.500019036233425e-06, 2.400018274784088e-06, 6.499991286545992e-06, 2.9999646358191967e-06, 2.600019797682762e-06, 2.300017513334751e-06, 2.400018274784088e-06, 2.100015990436077e-06, 2.0999577827751637e-06, 2.200016751885414e-06, 2.400018274784088e-06],
          'fibonacci_iterative': [4.449998959898949e-05, 4.959997022524476e-05, 6.150000263005495e-05, 7.990002632141113e-05, 0.00011189997894689441, 0.00013920001219958067, 0.00018919998547062278, 0.00026379997143521905, 0.0003637999761849642, 0.0004832999547943473, 0.0006852000369690359, 0.0013253000215627253, 0.0023447000421583652, 0.0035587000311352313, 0.005158300045877695, 0.009173200000077486],
          'fibonacci_recursive_cache': [1.3500044587999582e-05, 8.800008799880743e-06, 7.199996616691351e-06, 9.400013368576765e-06, 1.1299969628453255e-05, 1.1700030881911516e-05, 1.3500044587999582e-05, 1.5400000847876072e-05, 1.7600017599761486e-05, 1.7799960914999247e-05, 1.9300030544400215e-05, 2.069998299703002e-05, 2.1799991372972727e-05, 2.2799998987466097e-05, 2.4500011932104826e-05, 2.5699962861835957e-05, 2.8800044674426317e-05],
          'fibonacci_bottom_up': [0.0001333000254817307, 0.00015660002827644348, 0.00021410000044852495, 0.0002601000014692545, 0.0003361999988555908, 0.0004653999931178987, 0.0005982000147923827, 0.0008251999970525503, 0.0011487000156193972, 0.001457099977415055, 0.002006000024266541, 0.0038025000249035656, 0.00674719997914508, 0.011427899997215718, 0.014585800003260374, 0.013542399974539876]}





# First approach to reach Fibonacci sequence
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Second approach to reach Fibonacci sequence
def fibonacci_iterative(n):
    a, b, c = 0, 1, 0
    if n == 0:
        return a
    for i in range(n):
        c = a + b
        a = b
        b = c

    return b


# Third approach to reach Fibonacci sequence
def fibonacci_binet(n):
    sqrt_5 = int(math.sqrt(5))
    phi = (1 + sqrt_5) // 2
    psi = (1 - sqrt_5) // 2
    return int((phi ** n - psi ** n) // sqrt_5)


# Fourth approach to reach Fibonacci sequence
def fibonacci_recursive_cache(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci_recursive_cache(n - 1, cache) + fibonacci_recursive_cache(n - 2, cache)
    return cache[n]


# Fifth approach to reach Fibonacci sequence
def fibonacci_matrix(n):
    def multiply(A, B):
        return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

    def power(A, n):
        if n == 1:
            return A
        if n % 2 == 0:
            half = power(A, n // 2)
            return multiply(half, half)
        else:
            return multiply(A, power(A, n - 1))

    if n == 0:
        return 0
    matrix = [[1, 1], [1, 0]]
    result_matrix = power(matrix, n - 1)
    return result_matrix[0][0]


# Sixth approach to reach Fibonacci sequence
def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


"""fibonacci_bottom_list = []
for i in test_for_other:
    start = time.perf_counter()
    n = fibonacci_bottom_up(i)
    end = time.perf_counter()
    print(n)
    fibonacci_bottom_list.append(end - start)

result['fibonacci_bottom_up'] = fibonacci_bottom_list

x = []
y = []
for i in result['fibonacci_bottom_up']:
    y.append(i)

plt.plot(test_for_other, y, label='Fibonacci_bottom')
plt.scatter(test_for_other, y)
plt.xlabel('n-th Fibonacci term')
plt.ylabel('Time (s)')
plt.title('Fibonacci_bottom')
plt.show()"""

Recursive_list = ["fibonacci_recursive", "fibonacci_recursive_cache"]
#Other: fibonacci_binet, fibonacci_iterative, fibonacci_matrix, fibonacci_bottom_up
myTable_recursive = PrettyTable(["Model"] + [str(i) for i in test_for_other])
"""for key in result:
    if key in Recursive_list:
        row_values = [key] + result[key]
        myTable_recursive.add_row(row_values)"""

a = 'fibonacci_bottom_up'
fibonacci_recursive_results = ["{:.3f}".format(value) for value in result[f'{a}']]

# Add a row for 'fibonacci_recursive' with formatted results
myTable_recursive.add_row([f"{a}"] + fibonacci_recursive_results)


print(myTable_recursive)
