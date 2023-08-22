from selenium.webdriver.common.by import By

from constants.registration import RegistrationConstants
from pages import utils
from pages.login import Login


class Registration(Login):
    """Store methods describes home page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = RegistrationConstants

    def sign_up(self, user):
        """Sign up using provided values"""

        self.fill_fields(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_fields(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_fields(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)
        self.fill_fields(xpath=self.const.SIGN_UP_CONFIRM_PASSWORD_FIELD_XPATH, value=user.password)

        self.click(self.const.SIGN_UP_BUTTON_XPATH)

    def verify_successful_registration(self):
        """Verify welcome text is displayed"""

        self.wait_until_displayed(by=By.XPATH, xpath=self.const.TEXT_AFTER_REGISTR_XPATH)

        assert self.compare_element_text(xpath=self.const.TEXT_AFTER_REGISTR_XPATH,
                                         text=self.const.TEXT_AFTER_REGISTRATION_TEXT)

    def terms_of_use_is_clickable(self):
        """Verify terms button is clickable"""

        self.is_element_clickable(xpath=self.const.TERMS_OF_USE_XPATH)

    def login_button_in_registration_form_is_clickable(self):
        """Verify Login button is clickable"""

        self.is_element_clickable(xpath=self.const.LOGIN_BUTTON_IN_REGFORM_XPATH)

    def verify_error_messages(self):
        """Verify name, email, password and confirm password are displayed error messages"""

        assert self.compare_element_text(xpath=self.const.NAME_ERROR_MESSAGE_XPATH,
                                         text=self.const.EMPTY_NAME_ERROR_MESSAGE_TEXT)

        assert self.compare_element_text(xpath=self.const.EMAIL_ERROR_MESSAGE_XPATH,
                                         text=self.const.EMAIL_ERROR_MESSAGE_TEXT)

        assert self.compare_element_text(xpath=self.const.PSW_ERROR_MESSAGE_XPATH,
                                         text=self.const.EMPTY_PSW_ERROR_MESSAGE_TEXT)

        assert self.compare_element_text(xpath=self.const.CONFIRM_PSW_ERROR_MESSAGE_XPATH,
                                         text=self.const.EMPTY_PSW_ERROR_MESSAGE_TEXT)

    def empty_sign_up(self, user):
        """Sign up with empty fields"""
        self.fill_and_clear_fields(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_and_clear_fields(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_and_clear_fields(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)
        self.fill_and_clear_fields(xpath=self.const.SIGN_UP_CONFIRM_PASSWORD_FIELD_XPATH, value=user.password)

    def sign_up_short_username(self):
        """Trigger error message by providing short username"""

        username = utils.random_str()
        self.fill_fields(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=username)

    def verify_short_username_error_message(self):
        """Verify error message about too short username is displayed"""

        assert self.compare_element_text(xpath=self.const.NAME_ERROR_MESSAGE_XPATH,
                                         text=self.const.SHORT_NAME_ERROR_MESSAGE_TEXT)

    def input_short_password(self):
        """Trigger error message by providing short password"""
        password = utils.random_text(length=2)
        self.fill_fields(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)

    def verify_short_password_error_message(self):
        """Verify error message about too short password is displayed"""
        assert self.compare_element_text(xpath=self.const.PSW_ERROR_MESSAGE_XPATH,
                                         text=self.const.SHORT_PSW_ERROR_MESSAGE_TEXT)

    def input_invalid_password(self):
        """Trigger error message by providing password without special characters"""
        password = utils.random_text(length=4)
        self.clear_field(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH)
        self.fill_fields(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)

    def verify_invalid_password_error_message(self):
        """Verify error message about invalid password is displayed"""
        assert self.compare_element_text(xpath=self.const.PSW_ERROR_MESSAGE_XPATH,
                                         text=self.const.INV_PSW_ERROR_TEXT)

    def input_invalid_confirmation_psw(self):
        """Trigger error message by providing invalid confirmation password"""
        password = f"{utils.random_text(length=4)}PwD!"
        self.fill_fields(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        confirmation_psw = utils.random_text(length=4)
        self.fill_fields(xpath=self.const.SIGN_UP_CONFIRM_PASSWORD_FIELD_XPATH, value=confirmation_psw)

    def verify_invalid_confirmation_password_error_message(self):
        """Verify error message about invalid confirmation password is displayed"""
        assert self.compare_element_text(xpath=self.const.CONFIRM_PSW_ERROR_MESSAGE_XPATH,
                                         text=self.const.INVALID_CONFIRM_PSW_ERROR_MESSAGE_TEXT)

    def close_registration_form(self):
        """Close the registration form"""
        self.click(xpath=self.const.CLOSE_REGISTRATION_FORM_BUTTON_XPATH)
