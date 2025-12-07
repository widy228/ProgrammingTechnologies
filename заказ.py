import time

class Заказ:
    счетчик_заказов = 0

    def __init__(self):
        self.заказанные_пиццы = []
        Заказ.счетчик_заказов += 1
        self.номер = Заказ.счетчик_заказов

    def __str__(self):
        res = f"Заказ №{self.номер}\n"
        for i, пицца in enumerate(self.заказанные_пиццы, 1):
            res += f"{i}. {пицца}\n"
        res += f"Сумма заказа: {self.сумма():.2f} р.\n"
        return res

    def добавить(self, пицца):
        self.заказанные_пиццы.append(пицца)
        print(f"Пицца {пицца.название} добавлена!")

    def сумма(self):
        return sum(пицца.цена for пицца in self.заказанные_пиццы)

    def выполнить(self):
        print("Заказ поступил на выполнение...")
        for i, пицца in enumerate(self.заказанные_пиццы, 1):
            print(f"{i}. {пицца.название}")
            пицца.подготовить()
            time.sleep(1)
            пицца.испечь()
            time.sleep(1)
            пицца.нарезать()
            time.sleep(1)
            пицца.упаковать()
            time.sleep(1)
            print()
        print(f"Заказ №{self.номер} готов! Приятного аппетита!")    