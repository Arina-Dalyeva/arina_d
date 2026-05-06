s = "aacc"
t = "ccac"


def isAnagram(s, t):
    lst = [0] * 26
    lts = [0] * 26
    for i in range(len(s)):
        lst[ord(s[i]) - 97] = lst[ord(s[i]) - 97] + 1
    for i in range(len(t)):
        lts[ord(t[i]) - 97] = lts[ord(t[i]) - 97] + 1
    if lst == lts:
        return True
    else:
        return False


def isAnagram_2(s: str, t: str):
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



def isAnagramm3 (s: str, t: str):
    d = {}
    x = {}
    for i in range (len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] +=1
    for j in range (len(t)):
        if t[j] not in x:
            x[t[j]] = 1
        else:
            x[t[j]] +=1
    if x == d:
        return True
    else:
        return False


print(isAnagramm3(s, t))
