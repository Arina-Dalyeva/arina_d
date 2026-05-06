d = {}


def golosovanie (d):
    i = 1
    while i <= 5:
        x = input()
        if x not in d:
            d[x] = 1
            print(d)
            i = i+1
        else:
            d[x] += 1
            print(d)
            i = i+1
    for item in d:
        print(item)
    return d


print(golosovanie(d))