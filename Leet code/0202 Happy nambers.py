n = 12


def happy_namber (n):
    z = []
    for digit in str(n):
        z.append(int(digit))
    d = {}
    while True:
        x = 0
        for i in range(len(z)):
            x = x + z[i]**2
        if x not in d:
            d[x] = 1
        else:
            return False
        if x == 1:
            return True
        z = []
        for digit in str(x):
            z.append(int(digit))
print(happy_namber(n))


def happy_namber_2 (n):
    def summa_kvadratov(x):
        for i in range(len(z)):
            x = x + z[i]**2
    z = []
    for digit in str(n):
        z.append(int(digit))
    d = {}
    while x != 1:
        x = 0
        print(summa_kvadratov(x))
        if x not in d:
            d[x] = 1
        else:
            return False
        z = []
        for digit in str(x):
            z.append(int(digit))
    return True
print(happy_namber(n))