"""Tests related to category page"""
import pytest

from constants.base import BaseConstants
from constants.home_page import HomePageConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestCategoryPage:
    """Stores tests for category page functionality"""

    @pytest.mark.parametrize("title_button", [HomePageConstants.CATEGORY_CHILDREN_WORLD_IMG_XPATH,
                                              HomePageConstants.CATEGORY_PROPERTY_IMG_XPATH,
                                              HomePageConstants.CATEGORY_CAR_IMG_XPATH,
                                              HomePageConstants.CATEGORY_TRANSPORT_IMG_XPATH,
                                              HomePageConstants.CATEGORY_PETS_IMG_XPATH,
                                              HomePageConstants.CATEGORY_HOME_IMG_XPATH,
                                              HomePageConstants.CATEGORY_WORK_IMG_XPATH,
                                              HomePageConstants.CATEGORY_BUSINESS_IMG_XPATH,
                                              HomePageConstants.CATEGORY_FASHION_IMG_XPATH,
                                              HomePageConstants.CATEGORY_RELAX_IMG_XPATH,
                                              HomePageConstants.CATEGORY_ELECTRO_IMG_XPATH,
                                              HomePageConstants.CATEGORY_FOR_FREE_IMG_XPATH,
                                              HomePageConstants.CATEGORY_HELP_IMG_XPATH,
                                              HomePageConstants.CATEGORY_EXCHANGE_IMG_XPATH,
                                              HomePageConstants.CATEGORY_REPAIR_IMG_XPATH,
                                              HomePageConstants.CATEGORY_VICTORY_IMG_XPATH])
    def test_mar81_category_name_on_category_page(self, home_page, title_button):
        """
         - Fixture: open home page
         - Steps:
             - navigate to category page (to check all categories?)
             - verify category name is displayed
        """

        category_page = home_page.navigate_to_category_page(title_button=title_button)
        category_page.verify_category_name_is_displayed(title_button=title_button)

    @pytest.fixture()
    def category_page(self, home_page):
        category_page = home_page.navigate_to_category_page(title_button=HomePageConstants.CATEGORY_RELAX_IMG_XPATH)
        return category_page

    def test_mar87_pagination(self, category_page):
        """
        - Fixture: navigate to the category page
        - Steps:
            - verify the pagination is displayed and clickable
        """
        category_page.verify_pagination_is_displayed_and_clickable()
