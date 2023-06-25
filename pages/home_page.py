from constants.home_page import HomePageConstants
from pages.base_page import BasePage


class HomePage(BasePage):
    """Store methods describes home page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = HomePageConstants

    def verify_categories_are_at_the_home_page(self):
        """Verify that categories are present on the home page"""

        assert self.is_element_exists(xpath=self.const.CATEGORIES_XPATH)
        assert self.is_element_visible(xpath=self.const.CATEGORIES_XPATH)
        assert self.compare_element_text(xpath=self.const.CATEGORIES_XPATH, text=self.const.CATEGORIES_TEXT)

    def verify_logo_at_home_page(self):
        """Verify logo is visible on the home page"""

        assert self.is_element_visible(xpath=self.const.LOGO_XPATH)
