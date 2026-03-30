lst = [1, -2, 3, -4, 5, -6, 7, 8, 9, 10, -11, -12, -13, -14, 15, 16, 17, 18, 19, 20]
s = 0
for i in range(0, len(lst), 1):
    if lst[i] > 0 and i % 2 != 0:
        s = s + lst[i]

print(s)
