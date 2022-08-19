class Human:

    default_name = "Виктор"
    default_age = 28

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self._house = False

    def info(self):
        print(
            f"Меня зовут {self.name}. Мне {self.age}. "
            f"У меня есть {self.__money}$"
        )
        if self._house:
            print("У меня есть дом.")
        else:
            print("У меня нет дома.")

    @staticmethod
    def default_info():
        print(
            f"Имя по умолчанию: {Human.default_name}. "
            f"Возраст по умолчанию: {Human.default_age}"
        )

    def __make_deal(self, obj, price):
        self.__money -= price
        self._house = True
        print(f"Вы купили {obj} за {price}$. Баланс: {self.__money}$")

    def earn_money(self, money):
        self.__money += money
        print(f"Баланс пополнен на {money}$. Баланс:{self.__money}$")

    def buy_house(self, obj, sale):
        final_price = obj.final_price(sale)
        if self.__money >= final_price:
            self.__make_deal(obj, final_price)
        else:
            print("Недостаточно средств. Пополните баланс.")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def __str__(self):
        return f"Дом площадью {self._area} м2"

    def final_price(self, sale):
        self._price = self._price / 100 * (100 - sale)
        return self._price

    def info(self):
        print(f"{self._area} and {self._price}")


class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)
