import random
import string
# from selenium.webdriver.firefox.options import Options

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from constants.base import BaseConstants
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def create_driver(browser):
    """Creates driver according to provided browser"""
    if browser == BaseConstants.CHROME:
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(service=service, options=options)
        # driver.maximize_window()
        # driver.set_window_size(1920, 1080)
    elif browser == BaseConstants.FIREFOX:
        options = webdriver.FirefoxOptions()
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(
            service=service, options=options)
        driver.maximize_window()
    else:
        raise ValueError(f"Unknown browser name: {browser}")
    driver.get(BaseConstants.URL)
    driver.implicitly_wait(1)
    return driver

# def create_driver(browser):
#     """Creates driver according to provided browser"""
#     if browser == BaseConstants.CHROME:
#         driver = webdriver.Chrome(
#             executable_path='/drivers/chromedriver')
#         driver.maximize_window()
#     elif browser == BaseConstants.FIREFOX:
#         options = Options()
#         # options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
#         driver = webdriver.Firefox(
#             executable_path='/drivers/geckodriver', options=options)
#         driver.maximize_window()
#     else:
#         raise ValueError(f"Unknown browser name: {browser}")
#     driver.get(BaseConstants.URL)
#     driver.implicitly_wait(1)
#     return driver


def random_num():
    """Generate random number"""
    return random.choice(string.digits)


def random_str():
    """Generate random string"""
    return random.choice(string.ascii_letters)


def random_text(length, text=''):
    """Generate random text"""
    for i in range(length):
        text += ''.join(random_str() + random_num())
    return text
