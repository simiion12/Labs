import random
dan = 0
danp = 0
ana = 0
anap = 0
total = 0
winan = 0
first = random.randint(1, 2)
def tennis(trs):
    global dan
    global ana
    global total
    global anap
    global danp
    global first
    global winan
    for i in range(trs):
        ana = 0
        dan = 0
        while ana < 26 or dan < 26:
            if first == 1:
                anap = random.random()
                if anap <= 0.7:
                    ana += 1
                    if ana == 25:
                        winan += 1
                        break
                    continue
                else:
                    first = 2
                    continue
            if first == 2:
                danp = random.random()
                if danp <= 0.5:
                    dan += 1
                    if dan == 25:
                        break
                else:
                    first = 1
        total += 1


tennis(10000)
print(winan/10000)




