import requests
from selenium.webdriver.common.by import By

from constants.home_page import HomePageConstants
from pages.base_page import BasePage


class HomePage(BasePage):
    """Store methods describes home page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = HomePageConstants

    def check_api_request(self):
        """Test request API for URL"""
        response = requests.get(url=self.const.API_URL)
        assert response.status_code == 200

    def verify_categories_are_at_the_home_page(self):
        """Verify that categories are present on the home page"""

        assert self.is_element_exists(xpath=self.const.CATEGORIES_XPATH)
        assert self.is_element_visible(xpath=self.const.CATEGORIES_XPATH)
        assert self.compare_element_text(xpath=self.const.CATEGORIES_XPATH, text=self.const.CATEGORIES_TEXT)

    def verify_logo_at_home_page(self):
        """Verify logo is visible on the home page"""
        # self.wait_until_displayed(by=By.XPATH, xpath=self.const.LOGO_XPATH)
        assert self.is_element_visible(xpath=self.const.LOGO_XPATH)

    def verify_category_title_is_clickable(self, title_button):
        """Verify category's title is clickable"""
        self.wait_until_clickable(by=By.XPATH, xpath=title_button)
        assert self.is_element_clickable(xpath=title_button)

    def verify_category_image_is_clickable(self, image):
        """Verify category's image is clickable"""
        self.wait_until_clickable(by=By.XPATH, xpath=image)
        assert self.is_element_clickable(xpath=image)

    def verify_footer_is_displayed_on_the_home_page(self):
        """Verify that the footer is presented on the home page"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.FOOTER_XPATH)
        assert self.is_element_visible(xpath=self.const.FOOTER_XPATH)

    def verify_header_is_displayed_on_the_home_page(self):
        """Verify that the header is presented on the home page"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.HEADER_XPATH)
        assert self.is_element_visible(xpath=self.const.HEADER_XPATH)

    def check_all_needed_articles_are_displayed_in_footer(self, article):
        """Check and verify all articles are present in the footer"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.FOOTER_XPATH)

        if article == self.const.TERMS_OF_USE_UKR_TEXT:
            assert self.is_element_clickable(xpath=self.const.TERMS_OF_USE_UKR_XPATH)
        elif article == self.const.SECURITY_POLICY_UKR_TEXT:
            assert self.is_element_clickable(xpath=self.const.SECURITY_POLICY_UKR_XPATH)
        elif article == self.const.HOW_TO_SELL_AND_BUY_UKR_TEXT:
            assert self.is_element_clickable(xpath=self.const.HOW_TO_SELL_AND_BUY_UKR_XPATH)
        elif article == self.const.SITE_MAP_UKR_TEXT:
            assert self.is_element_clickable(xpath=self.const.SITE_MAP_UKR_XPATH)

    def verify_appropriate_category_images(self, title_button):
        """Verify appropriate category's images are displayed at the home page"""
        self.wait_until_displayed(by=By.XPATH, xpath=title_button)

        if title_button == self.const.CATEGORY_CHILDREN_WORLD_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_CHILDREN_WORLD_IMG_XPATH)
        elif title_button == self.const.CATEGORY_PROPERTY_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_PROPERTY_IMG_XPATH)
        elif title_button == self.const.CATEGORY_CAR_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_CAR_IMG_XPATH)
        elif title_button == self.const.CATEGORY_TRANSPORT_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_TRANSPORT_IMG_XPATH)
        elif title_button == self.const.CATEGORY_PETS_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_PETS_IMG_XPATH)
        elif title_button == self.const.CATEGORY_HOME_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_HOME_IMG_XPATH)
        elif title_button == self.const.CATEGORY_WORK_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_WORK_IMG_XPATH)
        elif title_button == self.const.CATEGORY_BUSINESS_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_BUSINESS_IMG_XPATH)
        elif title_button == self.const.CATEGORY_FASHION_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_FASHION_IMG_XPATH)
        elif title_button == self.const.CATEGORY_RELAX_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_RELAX_IMG_XPATH)
        elif title_button == self.const.CATEGORY_ELECTRO_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_ELECTRO_IMG_XPATH)
        elif title_button == self.const.CATEGORY_FOR_FREE_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_FOR_FREE_IMG_XPATH)
        elif title_button == self.const.CATEGORY_HELP_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_HELP_IMG_XPATH)
        elif title_button == self.const.CATEGORY_EXCHANGE_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_EXCHANGE_IMG_XPATH)
        elif title_button == self.const.CATEGORY_REPAIR_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_REPAIR_IMG_XPATH)
        elif title_button == self.const.CATEGORY_VICTORY_TITLE_XPATH:
            assert self.is_element_visible(xpath=self.const.CATEGORY_VICTORY_IMG_XPATH)

    def navigate_to_category_page(self, title_button):
        """Navigate to the category page by clicking on the category"""
        self.wait_until_displayed(by=By.XPATH, xpath=title_button)
        self.click(xpath=title_button)

        from pages.category_page import CategoryPage
        return CategoryPage(self.driver)
