from constants.single_product_page import SingleProductPageConst
from pages import utils, text_presets
from pages.base_page import BasePage
from pages.home_page import HomePage


class SingleProductPage(BasePage):
    """Store methods describes home page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = SingleProductPageConst
        self.home_page = HomePage(self.driver)

    def create_new_valid_notice(self, category, city):
        """Add new notice"""
        # input title
        self.fill_fields(xpath=self.const.CREATE_TITLE_INPUT_XPATH, value=utils.random_text(3))

        # input description
        self.fill_fields(xpath=self.const.CREATE_DESCR_INPUT_XPATH, value=text_presets.NOTICE_DESCRIPTION)

        # choose category
        if category == "Авто":
            self.click(xpath=self.const.AUTO_NOTICE_CATEGORY_XPATH),
        elif category == "Бізнес та послуги":
            self.click(xpath=self.const.BUSINESS_NOTICE_CATEGORY_XPATH),
