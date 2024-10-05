import random
tails = 0
heads = 0
total = 0
win = 0
j = 0
def coin_game(trials):
    global tails
    global heads
    global total
    global win
    global j
    while j < trials:
        j += 1
        for i in range(trials):
            flip = random.randint(1, 2)
            if flip == 1:
                tails += 1
                win += 2 ** tails
            elif flip == 2 and tails == 0:
                tails = 0
                win += 2
                break
            else:
                tails = 0
                break
            total += 1





coin_game(100000)
pay_1 = win / total
print (pay_1)
