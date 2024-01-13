import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
x = []
y = []
x1 = []
y1 = []
def nine_sum(trials):
    flips = 0
    for i in range(trials):
        x.append(i)
        flip1 = random.randint(1, 6)
        flip2 = random.randint(1, 6)
        flip3 = random.randint(1, 6)
        if flip1 + flip2 + flip3 == 9:
           flips += 1
        y.append(flips)

def ten_sum(trials):
    flips = 0
    for i in range(trials):
        x1.append(i)
        flip1 = random.randint(1, 6)
        flip2 = random.randint(1, 6)
        flip3 = random.randint(1, 6)
        if flip1 + flip2 + flip3 == 10:
            flips += 1
        y1.append(flips)


nine_sum(50000)
ten_sum(50000)
plt.plot(x, y)
plt.plot(x1, y1)
plt.show()