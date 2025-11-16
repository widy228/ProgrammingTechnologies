a = int(input())
b = int(input())

c = [a, b]
c = sorted(c)
print(c[0], c[1])

c = sorted(c, reverse=True)
print(c[0])
print(c[1])