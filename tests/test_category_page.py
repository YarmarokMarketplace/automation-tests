"""Tests related to category page"""
import pytest

from constants.base import BaseConstants
from constants.home_page import HomePageConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestCategoryPage:
    """Stores tests for category page functionality"""

    @pytest.mark.parametrize("title_button", [HomePageConstants.CATEGORY_CHILDREN_WORLD_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_PROPERTY_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_CAR_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_TRANSPORT_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_PETS_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_HOME_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_WORK_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_BUSINESS_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_FASHION_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_RELAX_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_ELECTRO_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_FOR_FREE_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_HELP_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_EXCHANGE_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_REPAIR_TITLE_XPATH,
                                              HomePageConstants.CATEGORY_VICTORY_TITLE_XPATH])
    def test_mar81_category_name_on_category_page(self, home_page, title_button):
        """
         - Fixture: open home page
         - Steps:
             - navigate to category page (to check all categories?)
             - verify category name is displayed
        """

        category_page = home_page.navigate_to_category_page(title_button=title_button)
        category_page.verify_category_name_is_displayed(title_button=title_button)
