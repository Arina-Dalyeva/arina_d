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




