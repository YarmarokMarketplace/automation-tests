from selenium.webdriver.common.by import By

from constants.login import LoginConstants
from pages.base_page import BasePage


class Login(BasePage):
    """Store methods describes home page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = LoginConstants

    def navigate_to_registration(self):
        """Navigate to the registration form"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.SIGN_UP_BUTTON_IN_LOGIN_XPATH)
        self.click(xpath=self.const.SIGN_UP_BUTTON_IN_LOGIN_XPATH)

        from pages.registration import Registration
        return Registration(self.driver)

    def login(self, user):
        """Login providing valid credentials"""
        self.fill_fields(xpath=self.const.LOGIN_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_fields(xpath=self.const.LOGIN_PASSWORD_FIELD_XPATH, value=user.password)

        self.wait_until_clickable(by=By.XPATH, xpath=self.const.LOGIN_BUTTON_XPATH)
        self.click(xpath=self.const.LOGIN_BUTTON_XPATH)

    def verify_username_in_the_header(self, user):
        """Verify successful login and username appears in the header"""

        self.compare_element_text(xpath=self.const.USERNAME_IN_THE_HEADER_XPATH,
                                  text=user.usernamename)

    def login_with_empty_credentials(self, user):
        """Login with empty credentials"""
        self.fill_and_clear_fields(xpath=self.const.LOGIN_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_and_clear_fields(xpath=self.const.LOGIN_PASSWORD_FIELD_XPATH, value=user.password)

    def verify_error_messages_in_login(self):
        """Verify email and password are displayed error messages"""

        assert self.compare_element_text(xpath=self.const.EMAIL_ERROR_MESSAGE_XPATH,
                                         text=self.const.EMAIL_EMPT_ERROR_MESSAGE_TEXT)

        assert self.compare_element_text(xpath=self.const.PSW_ERROR_MESSAGE_XPATH,
                                         text=self.const.PSW_EMPT_ERROR_MESSAGE_TEXT)

    def verify_error_messages_without_registration(self):
        """Verify email and password are displayed error messages"""

        assert self.compare_element_text(xpath=self.const.EMAIL_ERROR_MESSAGE_XPATH,
                                         text=self.const.ERROR_WITHOURT_REGISTRATION_TEXT)

        assert self.compare_element_text(xpath=self.const.PSW_ERROR_MESSAGE_XPATH,
                                         text=self.const.ERROR_WITHOURT_REGISTRATION_TEXT)

    def navigate_to_forget_password_form(self, user):
        """Click the forget password"""
        self.fill_fields(xpath=self.const.LOGIN_EMAIL_FIELD_XPATH, value=user.email)
        self.click(xpath=self.const.FORGET_PASSWORD_BUTTON)

    def verify_reset_password_form_is_displayed(self):
        """Verify that the forget-password page is opened"""
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.RESET_PASSWORD_HEADER_XPATH)
        assert self.compare_element_text(xpath=self.const.RESET_PASSWORD_HEADER_XPATH,
                                         text=self.const.RESET_PASSWORD_HEADER_TEXT)
