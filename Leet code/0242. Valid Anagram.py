s = "aacc"
t = "ccac"


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    t = list(t)
    for i in range(len(s)):
        if s[i] in t:
            t.remove(s[i])
    if len(t) == 0:
        return True
    else:
        return False


print(isAnagram(s, t))
lst[ord('b')-97]



