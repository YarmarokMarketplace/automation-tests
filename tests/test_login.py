"""Tests related to registration form"""
import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestRegistration:
    """Stores tests for registration functionality"""

    @pytest.fixture()
    def login(self, home_page):
        login = home_page.navigate_to_login()
        return login

    # def test_mar26_valid_login(self, login, random_user):
    #     """
    #     - Steps:
    #         - click login button
    #         - click registration button
    #         - sign up
    #         - verify user is registered
    #         - close registration
    #         - click login button
    #         - login
    #         - verify successful login
    #     """
    #     registration = login.navigate_to_registration()
    #     registration.sign_up(user=random_user)
    #     registration.verify_successful_registration()
    #     registration.close_registration_form()
    #     login.login(user=random_user)
    #     login.verify_username_in_the_header(name=random_user)
    #
    def test_mar26_empty_login(self, login, random_user):
        """
        - Steps:
            - click login button
            - login with empty credentials
            - verify error messages
        """
        login.login_with_empty_credentials(user=random_user)
        login.verify_error_messages_in_login()

    def test_mar26_login_without_registration(self, login, random_user):
        """
        - Steps:
            - click login button
            - login without registration
            - verify error messages
        """
        login.login(user=random_user)
        login.verify_error_messages_without_registration()

    # def test_mar36_forget_password(self, login, random_user):
    #     """
    #     - Steps:
    #         - click login button
    #         - fill email
    #         - click forget-password button
    #         - verify reset-password form is displayed
    #     """
    #     login.navigate_to_forget_password_form(user=random_user)
    #     login.verify_reset_password_form_is_displayed()
