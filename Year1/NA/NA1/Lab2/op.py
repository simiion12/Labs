import numpy as np

import matplotlib.pyplot as plt

def newton_Int(x1, y1, z):
    # Initialize k to 1 and Q to a list of zeros to hold the coefficients
    n = len(x1)
    a = y1.copy()
    # Calculate the divided differences using nested loops
    for j in range(1, n):
        for i in range(n-1, j - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (x1[i] - x1[i - j])
    # Calculate the coefficients of the polynomial using the divided differences
    p = a[-1]
    for i in range(n-2, -1, -1):
        p = a[i] + (z - x1[i]) * p
    # Return the value of the polynomial at the given point x
    return p


def bartles_stewart2(x1, y1, z, degree= 3):
    p = np.polyfit(x1, y1, degree)
    return np.polyval(p, z)

# read in the data from text file
with open("dataset_2.txt") as f:
    lines = f.readlines()

# parse the data into arrays
x1 = []
y1 = []
days = 1
for line in lines:
    if line.startswith("Date"):  # skip the header line
        continue
    date, visitors = line.strip().split(",")
    if visitors == 'Nan':
        visitors = newton_Int(x1[-10:],y1[-10:],days - 1)
    x1.append(days)
    y1.append(int(visitors))
    days += 1

print(x1)
print(y1)


from scipy.interpolate import CubicSpline
spline = CubicSpline(x1, y1)

x2, y2 = [], []
total_days = 16
z = len(x1)

x3, y3 = [], []


print(bartles_stewart2(x1, y1, 95))
print(spline(95))
# Finding through a loop the rest values for visitors
for rest_days in range(total_days):
    #k = bartles_stewart2(x1[-10:],y1[-10:],z)
    k = newton_Int(x1[-11:], y1[-11:], z)
    x2.append(z + 1)
    y2.append(k)
    o = spline(z)
    x3.append(z + 1)
    y3.append(o)
    z += 1

plt.plot(x1, y1, 'o', label='Original data')
plt.plot(x2, y2, '-', label='Interpolated data')
plt.legend()
plt.show()

plt.plot(x1, y1, 'o', label='Original data')
plt.plot(x3, y3, '--', label='Interpolated data')
plt.legend()
plt.show()