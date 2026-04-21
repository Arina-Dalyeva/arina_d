haystack = "abc"
needle = "c"


def strStr(haystack, needle):
    if haystack == needle:
        return 0
    for j in range(0, len(haystack)-len(needle)+1, 1):
        s = haystack[j:len(needle)+j:1]
        print(s)
        if s == needle:
            return j 
    return -1


print(strStr(haystack, needle))