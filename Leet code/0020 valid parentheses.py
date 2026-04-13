from fileinput import close

s = "){"
def isValid(s) -> bool:
    open_bracket = '[({'
    close_bracket = '])}'
    lst = []
    if len(s) == 1:
        return False
    for i in range (len(s)):
        if s[i] in open_bracket:
            lst.append(s[i])
        elif s[i] in close_bracket:
            if len(lst) == 0:
                return False
            elif close_bracket.index(s[i]) != open_bracket.index(lst[-1]):
                return False
            else:
                lst.pop()
    if len(lst) == 0:
        return True
    else:
        return False
print(isValid(s))

