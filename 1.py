info = {}
info["фио"] = "Петров Петр Петрович"
info["дата_рождения"] = "10.02.1999"
info["место_рождения"] = "Москва"

print(info)

info["хобби"] = ["плавание", "шахматы"]
info["хобби"].append("программирование")

info["животные"] = ("кот Том")

info["ЕГЭ"] = {}
info["ЕГЭ"]["русский язык"] = "87"
info["ЕГЭ"]["математика"] = "97"
info["ЕГЭ"]["информатика"] = "74"
info["ЕГЭ"]["химия"] = ""
del info["ЕГЭ"]["химия"]

info["вузы"] = {}
info["вузы"]["МГУ"] = "299"
info["вузы"]["ВГУИТ"] = "230"
info["вузы"]["ВГУ"] = "240"


print("\nДанные:\n", info)
exams = ", ".join(sorted([str(key) for key in info["ЕГЭ"].keys()]))
print("Предметы:", exams)

uni = ", ".join([str(key) for key in info["вузы"].keys()])
print("Вузы:", uni)

print("\nОтветы на вопросы:")

name = info.get("фио")
vowels = tuple("аоуыэяёюие")
starts_with_vowel = name[0] in vowels

print("* мое имя начинается на гласную букву:", starts_with_vowel)
month = info.get("дата_рождения").split(".")[1]
winter_or_summer = ("12", "01", "02", "06", "07", "08")
born_in_winter_or_summer = month in winter_or_summer

print("* родился летом или зимой:", born_in_winter_or_summer)

hobbies_count = len(info.get("хобби"))
print(f"* у меня {hobbies_count} хобби, первое \"{info.get("хобби")[0]}\"")

print(f"* после окончания школы сдавал {len(info.get("ЕГЭ"))} экз.")

sum_mark = int(info["ЕГЭ"].get("русский язык")) + int(info["ЕГЭ"].get("математика")) + int(info["ЕГЭ"].get("информатика"))
print(f"* сумма баллов = {sum_mark}")

max_mark = max(int(info["ЕГЭ"].get("русский язык")), int(info["ЕГЭ"].get("математика")), int(info["ЕГЭ"].get("информатика")))
print(f"* макс. балл = {max_mark}")

vuz_count = 0
if int(info["вузы"].get("МГУ")) < sum_mark:
    vuz_count += 1
if int(info["вузы"].get("ВГУИТ")) < sum_mark:
    vuz_count += 1
if int(info["вузы"].get("ВГУ")) < sum_mark:
    vuz_count += 1        
    
print(f"* кол-во вузов в которые прохожу: {vuz_count}")    
