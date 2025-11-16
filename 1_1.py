a = input()
a = a.split(" ")
f = open('1_1.txt', 'w')

for i in a:
    f.write(i + '\n')

f.close()    