from selenium.webdriver.common.by import By

from constants.registration import RegistrationConstants
from pages.base_page import BasePage


class Registration(BasePage):
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

        self.is_element_clickable(xpath=self.const.LOGIN_BUTTON_XPATH)

    def verify_error_messages(self):
        """Verify name, email, password and confirm password are displayed error messages"""

        self.is_element_visible(xpath=self.const.NAME_ERROR_MESSAGE_XPATH)
        assert self.compare_element_text(xpath=self.const.NAME_ERROR_MESSAGE_XPATH,
                                         text=self.const.EMPTY_NAME_ERROR_MESSAGE_TEXT)

        self.is_element_visible(xpath=self.const.EMAIL_ERROR_MESSAGE_XPATH)
        assert self.compare_element_text(xpath=self.const.EMAIL_ERROR_MESSAGE_XPATH,
                                         text=self.const.EMAIL_ERROR_MESSAGE_XPATH)

        self.is_element_visible(xpath=self.const.PSW_ERROR_MESSAGE_XPATH)
        assert self.compare_element_text(xpath=self.const.PSW_ERROR_MESSAGE_XPATH,
                                         text=self.const.EMPTY_PSW_ERROR_MESSAGE_TEXT)

        self.is_element_visible(xpath=self.const.CONFIRM_PSW_ERROR_MESSAGE_XPATH)
        assert self.compare_element_text(xpath=self.const.CONFIRM_PSW_ERROR_MESSAGE_XPATH,
                                         text=self.const.EMPTY_PSW_ERROR_MESSAGE_TEXT)

    def empty_sign_up(self, user):
        """Sign up using provided values"""

        self.fill_fields(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.clear(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH)
        # self.fill_fields(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH, value=user.email)
        # self.clear(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH)
        # self.fill_fields(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)
        # self.clear(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH)
        # self.fill_fields(xpath=self.const.SIGN_UP_CONFIRM_PASSWORD_FIELD_XPATH, value=user.password)
        # self.clear(xpath=self.const.SIGN_UP_CONFIRM_PASSWORD_FIELD_XPATH)
