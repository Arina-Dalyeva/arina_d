digits = [9, 9]

def plusOne(digits):
    x = ('')
    for i in range(len(digits)):
        digits[i] = str(digits[i])
        x = x + digits[i]
    print(x)
    x = int(x)
    print(x)
    x += 1
    print(x)
    x = str(x)
    z = []
    for digit in str(x):
        z.append(int(digit))
    return z


print(plusOne(digits))