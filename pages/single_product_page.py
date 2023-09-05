from constants.single_product_page import SingleProductPageConst
from pages.base_page import BasePage
from pages.home_page import HomePage


class SingleProductPage(BasePage):
    """Store methods describes home page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = SingleProductPageConst
        self.home_page = HomePage(self.driver)

    def create_new_valid_notice(self):
        """Add new notice"""
        self.fill_fields()
