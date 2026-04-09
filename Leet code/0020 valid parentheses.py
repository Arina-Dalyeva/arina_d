s = "())"
def isValid(s) -> bool:
    x = 0
    for i in range (len(s)):
        if s[i] == '(':
            x = x + 1
        elif s[i] == ')':
            x = x - 1
        if x < 0:
            return False
    if x == 0:
        return True
    else:
        return False
print(isValid(s))