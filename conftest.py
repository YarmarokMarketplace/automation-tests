import pytest as pytest

from pages.home_page import HomePage
from pages.utils import create_driver


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
