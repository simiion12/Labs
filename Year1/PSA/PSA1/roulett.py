import random


def adiacent(bllt, bullets):
    revolver_bullets = []
    for i in range(bullets):
        revolver_bullets.append(0)
    flip = random.randint(1, bullets)
    if (flip == bullets):
        revolver_bullets[0] = 1
        revolver_bullets[bullets - 1] = 1
    elif (flip != bullets):
        revolver_bullets[flip - 1] = 1
        revolver_bullets[flip] = 1
    return revolver_bullets


def nonadiacent(bllt, bullets):
    revolver_bullets = []
    for i in range(bullets):
        revolver_bullets.append(0)
    flip1 = random.randint(1, bullets)
    if (flip1 == bullets):
        revolver_bullets[flip1 - 1] = 1
    else:
        revolver_bullets[flip1] = 1
    flip2 = random.randint(1, bullets)
    if (flip2 == flip1 or flip2==flip1+1 or flip2==flip1-1 or (flip2==1 and flip1==bullets)):
        while (flip2 == flip1 or flip2==flip1+1 or flip2==flip1-1 or (flip2==1 and flip1==bullets)):
            flip2 = random.randint(1, bullets)
    if (flip2 == bullets):
        revolver_bullets[flip2 - 1] = 1
    else:
        revolver_bullets[flip2] = 1
    return revolver_bullets


def spin(bullets, total, trs, revolver_bullets):
    deaths = 0
    for i in range(trs):
        pick = random.randint(0, total - 1)
        if (revolver_bullets[pick] == 1):
            deaths = deaths + 1
    return 1 - (deaths / trs)


def nospin(bullets, total, trs, revolver_bullets):
    deaths = 0
    died1 = 0
    for i in range(trs):
        pick = random.randint(0, total - 1)
        if (revolver_bullets[pick] == 0):
            if (pick == total - 1):
                if (revolver_bullets[0] == 1):
                    deaths += 1
            else:
                if (revolver_bullets[pick + 1] == 1):
                    deaths += 1
        elif (revolver_bullets[pick] == 1):
            died1 += 1
    return 1 - deaths / (trs - died1)


def spinad(bullets, total, trs):
    pist = adiacent(bullets, total)
    return spin(bullets, total, trs, pist)


def nospinad(bullets, total, trs):
    pist = adiacent(bullets, total)
    return nospin(bullets, total, trs, pist)


def spinnad(bullets, total, trs):
    pist = nonadiacent(bullets, total)
    return spin(bullets, total, trs, pist)


def nospinnad(bullets, total, trs):
    pist = nonadiacent(bullets, total)
    return nospin(bullets, total, trs, pist)



def printad(bul, rev, trs):
    print("spining adiacent bullets in ", rev , "revolv:", spinad(bul, rev, trs));
    print("non spining adiacent bullets in ", rev , " revolv:", nospinad(bul, rev, trs));


def printnonad(bul, rev, trs):
    print("spining non adiacent bullets in ", rev , " revolv: ", nospinnad(bul, rev, trs))
    print("non spining non adiacent bullets in ", rev , " revolv:", spinnad(bul, rev, trs))


trs = 1000000
printad(2, 6, trs)
printad(2, 5, trs)
printnonad(2, 6, trs)
printnonad(2, 5, trs)
