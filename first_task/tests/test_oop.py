from oop import Human


def test_human_create(create_man):
    assert Human.default_name == "Виктор", "Задайте имя по умолчанию."
    assert Human.default_age == 28, "Задайте возраст по умолчанию."
    assert create_man.age == 30, "Ошибка в создании объекта класса Human"
    assert create_man.name == "Вася", "Ошибка в создании объекта класса Human"


def test_house_create(create_small_house):
    assert (
        create_small_house._area == 40
    ), "Площадь объекта SmallHouse должна быть 40м2"


def test_buy_house_without_money(create_man, create_small_house):
    create_man.buy_house(create_small_house, 0)
    assert (
        create_man._house is False
    ), "Баланс меньше стоимости дома. Покупка невозможна!"


def test_buy_house_with_money(create_man, create_small_house):
    create_man.earn_money(10000)
    create_man.buy_house(create_small_house, 0)
    assert create_man._house is True, "Ошибка при покупке дома"
