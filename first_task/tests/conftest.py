import pytest
from oop import Human, SmallHouse


@pytest.fixture()
def create_man():
    man = Human("Вася", 30)
    return man


@pytest.fixture()
def create_small_house():
    small_house = SmallHouse(2000)
    return small_house
