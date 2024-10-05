#p = 47
#q = 59
p = int(input())
q = int(input())
a = input()
n = p * q
fi = (p - 1) * (q - 1)
d = 157
e = 0
while (d * e) % fi != 1:
    e += 1
x = []
for i in range(len(a)):
    c = (ord(a[i]) ** e) % n
    print(c, end = " ")
    x.append(c)
print()
for i in range(len(x)):
    x[i] = chr((x[i] ** d) % n)
    print(x[i], end=" ")
