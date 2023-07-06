"""Tests related to category page"""
import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestCategoryPage:
    """Stores tests for category page functionality"""

    def test_mar81_category_name_on_category_page(self, home_page):
        """
         - Fixture: open home page
         - Steps:
             - navigate to category page (to check all categories?)
             - verify category name is displayed
        """

        category_page = home_page.navigate_to_category_page()
        category_page.verify_category_name_is_displayed()

    def test_mar82_filter_products_by_price_api(self, driver):
        """
         - Fixture: open home page, navigate to category page (all?)
         - Steps:
             - send api request and verify response
        """
    #  Send api request and verify response
    #  api_request_sort_by()
