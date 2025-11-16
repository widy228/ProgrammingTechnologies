from _collections_abc import Hashable

a = [1, 2, 4, 5, 8, 5, 8, 'ad', 23, 'asff', 343, '34rf0']
b = []
for i in a:
    if isinstance(i, Hashable):
        b.append(i)

b = tuple(b)
print(b)        