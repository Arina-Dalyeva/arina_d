x = int(input('введите число'))
s = 0
while x > 0:
    s = s + x % 10
    x//= 10
print(s)
