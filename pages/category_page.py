from selenium.webdriver.common.by import By

from constants.category_page import CategoryPageConstants
from pages.base_page import BasePage
from pages.home_page import HomePage


class CategoryPage(BasePage):
    """Store methods describes home page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = CategoryPageConstants
        self.home_page = HomePage(self.driver)

    def verify_category_name_is_displayed(self, title_button):
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.HEAD_TITLE_XPATH)

        if title_button == self.home_page.const.CATEGORY_CHILDREN_WORLD_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_CHILDREN_WORLD_TITLE_TEXT)
        elif title_button == self.home_page.const.CATEGORY_PROPERTY_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_PROPERTY_TITLE_TEXT)
        elif title_button == self.home_page.const.CATEGORY_CAR_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_CAR_TITLE_TEXT)
        elif title_button == self.home_page.const.CATEGORY_TRANSPORT_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_TRANSPORT_TITLE_TEXT)
        elif title_button == self.home_page.const.CATEGORY_PETS_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_PETS_TITLE_TEXT)
        elif title_button == self.home_page.const.CATEGORY_HOME_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_HOME_TITLE_TEXT)
        elif title_button == self.home_page.const.CATEGORY_WORK_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_WORK_TITLE_TEXT)
        elif title_button == self.home_page.const.CATEGORY_BUSINESS_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_BUSINESS_TITLE_TEXT)
        elif title_button == self.home_page.const.CATEGORY_FASHION_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_FASHION_TITLE_TEXT)
        elif title_button == self.home_page.const.CATEGORY_RELAX_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_RELAX_TITLE_TEXT)
        elif title_button == self.home_page.const.CATEGORY_ELECTRO_TITLE_XPATH:
            assert self.compare_element_text(xpath=self.const.HEAD_TITLE_XPATH,
                                             text=self.home_page.const.CATEGORY_ELECTRO_TITLE_TEXT)

    def verify_pagination_is_displayed_and_clickable(self):
        """Verify pagination is displayed on the category page, and it's clickable"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.HEAD_TITLE_XPATH)
        assert self.is_element_visible(xpath=self.const.PAGINATION)
        assert self.is_element_clickable(xpath=self.const.PAGINATION)
