import random

import pytest as pytest

from pages.home_page import HomePage
from pages.utils import create_driver
from pages.values import User


@pytest.fixture()
def driver(browser):
    """Create selenium driver"""
    driver = create_driver(browser=browser)
    yield driver
    driver.close()


@pytest.fixture()
def home_page(driver):
    """Create home page object"""
    return HomePage(driver)


@pytest.fixture()
def empty_user():
    """Create empty user"""
    return User()


@pytest.fixture()
def random_user(empty_user):
    """Create random user"""
    empty_user.fill_data()
    return empty_user


@pytest.fixture()
def random_category():
    """Choose random category from the list"""
    categories = ["Авто", "Бізнес та послуги", "Безкоштовно", "Дитячий світ", "Дім і сад",
                  "Допомога", "Електроніка", "Запчастини для транспорту", "Мода і стиль",
                  "Нерухомість", "Обмін", "Ремонт", "Робота", "Тварини", "Товари для перемоги",
                  "Хобі, відпочинок і спорт"]
    return random.choice(categories)


@pytest.fixture()
def random_city():
    """Choose random city from the list"""
    cities = ["Київ", "Дніпро", "Харків", "Одеса", "Львів", "Херсон"]
    return random.choice(cities)
