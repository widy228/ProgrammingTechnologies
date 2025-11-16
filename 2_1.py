a = []

while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)
print(f"sum: {sum(a)}, count: {len(a)}")    