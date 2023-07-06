import requests
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

    def api_request_sort_by(self):
        """Send api requests to verify sort feature"""

        for sort in self.const.SORT_TYPES:
            url_server = self.const.URL_SERVER.format(sort=sort)

            payload = {}
            headers = {}

            response = requests.request("GET", url_server, headers=headers, data=payload)
            assert response.status_code == 200

        # ToDo: to come up how to connect this function with driver and use in test

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
