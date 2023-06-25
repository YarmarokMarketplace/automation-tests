from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Describes base methods for the website"""

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    def wait_until_displayed(self, by, xpath):
        """Wait until element is displayed and return it, else raise an exception"""
        return self.waiter.until(
            method=expected_conditions.visibility_of_element_located(
                (by, xpath)
            )
        )

    def wait_until_displayed_elements(self, by, xpath):
        """Wait until element is displayed and return it, else raise an exception"""
        return self.waiter.until(
            method=expected_conditions.visibility_of_all_elements_located(
                (by, xpath)
            )
        )

    def wait_until_clickable(self, by, xpath):
        """Wait until element is clickable and return it, else raise an exception"""
        return self.waiter.until(
            method=expected_conditions.element_to_be_clickable(
                (by, xpath)
            )
        )

    def is_element_exists(self, xpath):
        """Check if element exists"""
        try:
            self.driver.find_element(by=By.XPATH, value=xpath)
            return True
        except (TimeoutError, NoSuchElementException):
            return False

    def is_element_visible(self, xpath):
        """Check if element visible"""
        try:
            self.wait_until_displayed(by=By.XPATH, xpath=xpath)
            return True
        except (TimeoutError, NoSuchElementException):
            return False

    def fill_fields(self, xpath, value):
        """Fill the fields using provided values"""
        field = self.wait_until_clickable(by=By.XPATH, xpath=xpath)
        field.clear()
        field.send_keys(value)

    def click(self, xpath):
        """Find and click on the element by provided xpath"""
        element = self.wait_until_clickable(by=By.XPATH, xpath=xpath).click()

    def compare_element_text(self, xpath, text, strip=False):
        """Compare element text to provided one"""
        element_text = self.wait_until_displayed(by=By.XPATH, xpath=xpath)
        if strip:
            return element_text.text.strip() == text
        else:
            return element_text.text == text
