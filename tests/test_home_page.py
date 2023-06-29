"""Tests related to home page"""
import pytest

from constants.base import BaseConstants
from constants.home_page import HomePageConstants


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
                                              HomePageConstants.CATEGORY_ALL_TITLE_XPATH])
    def test_mar76_clicking_on_the_category_title(self, home_page, title_button):
        """
        - Steps:
            - open page (fixture)
            - verify category title is clickable
        """
        # Verify category title is clickable
        home_page.verify_category_title_is_clickable(title_button=title_button)

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

    @pytest.mark.parametrize("article", [HomePageConstants.TERMS_OF_USE_UKR_TEXT,
                                         HomePageConstants.SECURITY_POLICY_UKR_TEXT,
                                         HomePageConstants.HOW_TO_SELL_AND_BUY_UKR_TEXT,
                                         HomePageConstants.SITE_MAP_UKR_TEXT])
    def test_mar74_articles_links_on_the_header(self, home_page, article):
        """
        - Steps:
            - open home page (fixture)
            - verify list of functionality at header
        """
        # Verify list of functionality at header
        home_page.check_all_needed_articles_are_displayed_in_footer(article=article)

    # def test_mar75_categories_images_are_displayed_on_the_home_page(self, home_page):
    #     """
    #     - Steps:
    #         - open home page (fixture)
    #         - verify category's images are displayed at the home page
    #     """
    #     # Verify category's images are displayed at the home page
