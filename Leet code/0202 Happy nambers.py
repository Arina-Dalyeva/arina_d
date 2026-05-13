f = 12


def Happy_namber (f):
    z = []
    for digit in str(f):
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
print(Happy_namber(f))