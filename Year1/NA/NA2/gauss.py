import numpy as np
import scipy.linalg



# Define the matrix A and the constants of the system of equations
A = np.array([[0, 1, 5, -7, 23, -1, 7, 8, 1, -5],
              [17, 0, -24, -75, 100, -18, 10, -8, 9, -50],
              [3, -2, 15, 0, -78, -90, -70, 18, -75, 1],
              [5, 5, -10, 0, -72, -1, 80, -3, 10, -18],
              [100, -4, -75, -8, 0, 83, -10, -75, 3, -8],
              [70, 85, -4, -9, 2, 0, 3, -17, -1, -21],
              [1, 15, 100, -4, -23, 13, 0, 7, -3, 17],
              [16, 2, -7, 89, -17, 11, -73, 0, -8, -23],
              [51, 47, -3, 5, -10, 18, -99, -18, 0, 12],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]])

b = np.array([-10, -40, -17, 43, -53, 12, -60, 100, -12, 100])


LU, piv = scipy.linalg.lu_factor(A)


x = scipy.linalg.lu_solve((LU, piv), b)


print(x)
import numpy as np

sol = [87.49970902, -55.75380417, 17.77411635, 32.04744366, 11.74397126, -94.36514182, 9.18489557, -8.10628054, 99.97509067, 52.53605364]

res = 0
for i in range(len(sol)-1):
    x = sol[i]
    res += x
print(res)

