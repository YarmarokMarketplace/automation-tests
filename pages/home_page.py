from selenium.webdriver.common.by import By

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
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.LOGO_XPATH)
        assert self.is_element_visible(xpath=self.const.LOGO_XPATH)

    def verify_category_title_is_clickable(self):
        """Verify category's title is clickable"""
        self.wait_until_clickable(by=By.XPATH, xpath=self.const.CATEGORY_PROPERTY_TITLE_XPATH)
        assert self.is_element_clickable(xpath=self.const.CATEGORY_PROPERTY_TITLE_XPATH)

    def verify_category_image_is_clickable(self):
        """Verify category's image is clickable"""
        self.wait_until_clickable(by=By.XPATH, xpath=self.const.CATEGORY_PROPERTY_IMG_XPATH)
        assert self.is_element_clickable(xpath=self.const.CATEGORY_PROPERTY_IMG_XPATH)

    def verify_footer_is_displayed_on_the_home_page(self):
        """Verify that the footer is presented on the home page"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.FOOTER_XPATH)
        assert self.is_element_visible(xpath=self.const.FOOTER_XPATH)

    def verify_header_is_displayed_on_the_home_page(self):
        """Verify that the header is presented on the home page"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.HEADER_XPATH)
        assert self.is_element_visible(xpath=self.const.HEADER_XPATH)
