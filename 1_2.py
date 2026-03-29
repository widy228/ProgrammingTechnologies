f = open('1_1.txt', 'r')
a = [int(i.strip()) for i in f]
f.close()

summa = str(sum(a))
maximum = str(max(a))
f = open('1_1.txt', 'a')
f.write(summa + "\n")
f.write(maximum + "\n")
f.close()