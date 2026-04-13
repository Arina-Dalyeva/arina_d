x = 1000021
def isPalindrome(x: int):
    x = str(x)
    if len(x) == 1:
        return True
    for i in range (len(x)//2):
        if x[i] != x[-i-1]:
            return False
    return True
print(isPalindrome(x))


def isPalindrome(x: int):
    if x < 0:
        return False
    elif x == 0:
        return True
    m = 0
    a = 1
    while a < 0:
        a * 10
        m = x // 10
        m = m * 10
        m = x // 100








