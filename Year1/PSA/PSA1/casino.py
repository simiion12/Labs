import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
x = []
y = []
x1 = []
y1 = []
def red(trials):
    wallet = 10000
    for i in range(trials):
        wallet -= 20
        x.append(i)
        flip = random.randint(1, 38)
        if flip < 18:
           wallet += 40
        y.append(wallet)

def number(trials):
    wallet = 10000
    for i in range(trials):
        wallet -= 20
        x1.append(i)
        flip = random.randint(1, 38)
        if flip == 1:
           wallet += 20*35
        y1.append(wallet)

red(500)
number(500)
plt.plot(x, y)
plt.plot(x1, y1)
plt.show()
