"""Tests related to registration form"""
import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestRegistration:
    """Stores tests for registration functionality"""

    @pytest.fixture()
    def registration(self, home_page):
        login = home_page.navigate_to_login()
        registration = login.navigate_to_registration()
        return registration

    # def test_mar20_valid_registration(self, registration, random_user):
    #     """
    #     - Steps:
    #         - click registration button
    #         - sign up
    #         - verify user is registered
    #     """
    #
    #     registration.sign_up(user=random_user)
    #     registration.verify_successful_registration()

    def test_mar20_terms_button_and_login_buttons(self, registration):
        """
        - Steps:
            - click registration button
            - verify Terms of use button is clickable
            - verify Login button is clickable
        """
        registration.terms_of_use_is_clickable()
        registration.login_button_in_registration_form_is_clickable()

    def test_mar20_empty_credentials(self, registration, random_user):
        """
        - Steps:
            - click registration button
            - input credentials and then delete them
            - verify Error messages are displayed
        """
        registration.empty_sign_up(user=random_user)
        registration.verify_error_messages()

    def test_mar20_short_username(self, registration):
        """
        - Steps:
            - click registration button
            - input in Username field too short username
            - verify error message is appeared
        """
        registration.sign_up_short_username()
        registration.verify_short_username_error_message()

    # def test_mar20_invalid_password(self, registration):
    #     """
    #     - Steps:
    #         - click registration button
    #         - input short password
    #         - verify error message short password
    #         - input password without special characters
    #         - verify error message invalid password
    #     """
    #     registration.input_short_password()
    #     registration.verify_short_password_error_message()
    #     registration.input_invalid_password()
    #     registration.verify_invalid_password_error_message()

    def test_mar20_invalid_confirmation_password(self, registration):
        """
        - Steps:
          - click registration button
          - input invalid confirmation password
          - verify error message invalid confirmation password
        """
        registration.input_invalid_confirmation_psw()
        registration.verify_invalid_confirmation_password_error_message()
