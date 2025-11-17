f = open('1_4.txt', 'r', encoding="utf-8")
for i in f:
    print(i, end='')
f.close()

f = open('1_4.txt', 'r', encoding="utf-8")
a = [i.strip().split(' ') for i in f]


vowels = 'аоуиэфеёюя'
consonants = 'бвгджзйклмнпрстфхцчшщ'

count_vowels = count_consonants = 0

for i in a:
    for j in i:
        if j[0].lower() in vowels:
            count_vowels += 1
        elif j[0].lower() in consonants:
            count_consonants += 1  

if count_consonants > count_vowels:
    print("\nНачинающихся на согласную больше")

elif count_vowels > count_consonants:
    print("\nНачинающихся на гласную больше")

f.close()