f = open('1_1.txt', 'r')
a = []
for i in f:
    try:
        a.append(int(i.strip()))
    except ValueError:
        continue    
f.close()

summa = str(sum(a))
maximum = str(max(a))
f = open('1_1.txt', 'a')
f.write(summa + "\n")
f.write(maximum + "\n")
f.close()