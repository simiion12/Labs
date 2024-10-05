import numpy as np
x2 = [1, 2, 3, 4, 5]
y2 = [0, 0, np.log(2), np.log(6), np.log(24)]


# Define a function to calculate the coefficients of the polynomial Q4(x) using the Newton method
def Newton_Q4(x):
    # Initialize k to 1 and Q to a list of zeros to hold the coefficients
    k = 1
    Q = [0] * 5
    Q[0] = y2[0]
    # Calculate the divided differences using nested loops
    for i in range(1, 5):
        for j in range(4, i - 1, -1):
            y2[j] = (y2[j] - y2[j - 1]) / (x2[j] - x2[j - i])

    # Calculate the coefficients of the polynomial using the divided differences
    for i in range(5):
        k *= (x - x2[i - 1])
        Q[0] += y2[i] * k

    # Return the value of the polynomial at the given point x
    return Q[0]
x = 2.5
res = Newton_Q4(x)
q_new = np.exp(res)
# Print the result
print(f"Another form of approximation Gamma in point {x} is {q_new}")
