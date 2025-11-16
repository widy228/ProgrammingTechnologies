a = (1, 3, 6, 7, 8, 9, 0, 1, 4, 6, 8, 9, 12)
element = 6
b = []
for i in range(len(a)):
    if a[i] == element:
        b.append(i)

if len(b) == 2:
    print(a[b[0]:b[1]+1])
elif len(b) == 1:
    print(a[b[0]:])
else:
    print(tuple())        
