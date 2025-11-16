a = []
b = []

a.append(4.5)
a.append(3.4)

a.extend([8.7, 1.3])

b.append(14.5)
b.append(3.4)

b.extend([8.7, 11.3])

a.insert(1, 100)
a.insert(3, 100)

b.insert(0, 200)
b.insert(2, 200)

print("Исходные списки:")
print(a)
print(b)

del a[0]
del b[0]

a.remove(100)
b.remove(200)

print("\nПосле удалений:")
print(a)
print(b)

sa = set(a)
sb = set(b)
sa_and_sb = sa & sb

print("\nУникальные элементы:")
print(sa, sb)
print("общие:", sa_and_sb)

c = a + b

c_asc = sorted(c)
c_desc = sorted(c, reverse=True)

sr_ar = sum(c[i] for i in range(1, len(c)+1, 2))/(len(c)/2)

num = 1
count = 0

for i in range(0, len(c), 2):
    num *= c[i]
    count += 1

sr_geom = round(num ** (1/count), 2)

c_max = max(c)

c_min = min(c)

print("\nИтоговые:")
print('3-й:', c)
print("Возрастание: ", c_asc)
print("Убывание: ", c_desc)
print(f'Ср. арифм. = {sr_ar}, ср. геом. = {sr_geom}')
print(f'Макс. и мин.: {c_max} {c_min}')