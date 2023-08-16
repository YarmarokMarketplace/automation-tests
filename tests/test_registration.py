"""Tests related to registration form"""
import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestRegistration:
    """Stores tests for registration functionality"""

    @pytest.fixture()
    def registration(self, home_page):
        registration = home_page.navigate_to_login()
        return registration

    # def test_mar20_positive_registration(self, registration, random_user):
    #     """
    #     - Steps:
    #         - click registration button
    #         - sign up
    #         - verify user is registered
    #     """
    #
    #     registration.sign_up(user=random_user)
    #     registration.verify_successful_registration()
    #
    # def test_mar20_terms_button_and_login_buttons(self, registration):
    #
    #     registration.terms_of_use_is_clickable()
    #     registration.login_button_in_registration_form_is_clickable()

    def test_mar20_empty_credentials(self, registration, random_user):
        registration.empty_sign_up(user=random_user)
        registration.verify_error_messages()
