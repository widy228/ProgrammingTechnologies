def isInt(n):
    return int(n) == float(n)

a = (1, 9, 8, 7, 6, 2, 33.5, 900, 92, 873)

for i in range(len(a)):
    if isInt(a[i]) == False:
        print(a)
        break
    else:
        if i == len(a)-1:
            a = sorted(a)
            print(a)
