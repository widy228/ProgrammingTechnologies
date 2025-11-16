str = "-9324jhre-324-qw-q4oo-3l;p-"
first = last = -20
for i in range(len(str)):
    if str[i].isalpha():
        if first != -20:
            last = i
        else:
            first = i
    else:
        continue
if last == -20 and first == -20:
    print("Букв в строке нет")
elif last == -20:
    last = first
    print(first, last)
else:    
    print(first, last)    