"""Tests related to home page"""
import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestHomePage:
    """Stores tests for home page functionality"""

    # def mar71_home_page_as_default_by_url(self, home_page):
    #     """
    #     - Steps:
    #         - navigate by URL
    #         - verify home page with categories in DB
    #     """

    def test_mar152_home_page_is_the_first_page_that_visitors_see(self, home_page):
        """
        - Steps:
            - open home page
            - verify categories at the home page
        """

        # Verify categories at the home page
        home_page.verify_categories_are_at_the_home_page()

    def test_mar72_marketplace_logo_on_the_home_page(self, home_page):
        """
        - Steps:
            - open home page
            - verify logo at home page
        """

        # Verify logo at home page
        home_page.verify_logo_at_home_page()

    # def mar73_footer_on_the_home_page(self, home_page):
    #     """
    #     - Steps:
    #         - open home page
    #         - verify footer is at home page
    #         - verify a list of info at footer
    #     """
    #
    # def mar73_header_on_the_home_page(self, home_page):
    #     """
    #     - Steps:
    #         - open home page
    #         - verify header is at home page
    #     """
    #
    # def mar74_articles_links_on_the_header(self, home_page):
    #     """
    #     - Steps:
    #         - open home page
    #         - verify list of functionality at header
    #     """
    #
    # def mar75_categories_with_images_on_the_home_page(self, home_page):
    #     """
    #     - Steps:
    #         - open home page
    #         - verify category's images at the home page
    #     """
    #
    # def mar76_clicking_on_the_category_title(self, home_page):
    #     """
    #     - Steps:
    #         - open page
    #         - verify category title is clickable
    #     """
    #
    # def mar76_clicking_on_the_category_image(self, home_page):
    #     """
    #     - Steps:
    #         - open page
    #         - verify category image is clickable
    #     """
    #
    # def mar77_part_of_categories_on_the_screen_in_the_mobile_version(self, home_page):
    #     """
    #     - Steps:
    #         - open page
    #         - verify part of categories are displayed in the mobile version
    #     """
    #
    # def mar78_scrolling_the_categories(self, home_page):
    #     """
    #     - Steps:
    #         - open page
    #         - verify categories are scrollable
    #     """
