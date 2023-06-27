"""Tests related to home page"""
import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestHomePage:
    """Stores tests for home page functionality"""

    def test_mar152_home_page_is_the_first_page_that_visitors_see(self, home_page):
        """
        - Steps:
            - open home page (fixture)
            - verify categories at the home page
        """

        # Verify categories at the home page
        home_page.verify_categories_are_at_the_home_page()

    def test_mar72_marketplace_logo_on_the_home_page(self, home_page):
        """
        - Steps:
            - open home page (fixture)
            - verify logo at home page
        """

        # Verify logo at home page
        home_page.verify_logo_at_home_page()

    def test_mar76_clicking_on_the_category_title(self, home_page):
        """
        - Steps:
            - open page (fixture)
            - verify category title is clickable
        """
        # Verify category title is clickable
        home_page.verify_category_title_is_clickable()

    def test_mar76_clicking_on_the_category_image(self, home_page):
        """
        - Steps:
            - open page (fixture)
            - verify category image is clickable
        """
        # Verify category image is clickable
        home_page.verify_category_image_is_clickable()

    def test_mar73_footer_is_presented_on_the_home_page(self, home_page):
        """
        - Steps:
            - open home page (fixture)
            - verify footer is at home page
        """
        # Verify footer is at home page
        home_page.verify_footer_is_displayed_on_the_home_page()

    def test_mar73_header_on_the_home_page(self, home_page):
        """
        - Steps:
            - open home page (fixture)
            - verify header is at home page
        """
        # Verify header is at home page
        home_page.verify_header_is_displayed_on_the_home_page()

    # def test_mar74_articles_links_on_the_header(self, home_page):
    #     """
    #     - Steps:
    #         - open home page (fixture)
    #         - verify list of functionality at header
    #     """
    #
    # def test_mar75_categories_with_images_on_the_home_page(self, home_page):
    #     """
    #     - Steps:
    #         - open home page (fixture)
    #         - verify category's images at the home page
    #     """

    # def test_mar77_part_of_categories_on_the_screen_in_the_mobile_version(self, home_page):
    #     """
    #     - Steps:
    #         - open home page (fixture)
    #         - verify part of categories are displayed in the mobile version
    #     """
    #
    # def test_mar78_scrolling_the_categories(self, home_page):
    #     """
    #     - Steps:
    #         - open home page (fixture)
    #         - verify categories are scrollable
    #     """
