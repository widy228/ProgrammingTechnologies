x = int(input())

if x >= 0:
    f = x ** (1/2) + x ** 2

if x < 0:
    f = 1 / x

print(round(f, 2))        