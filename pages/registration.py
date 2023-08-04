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

        self.click(self.const.SIGN_UP_BUTTON_XPATH)
        # from pages.hello_page import HelloPage
        # return HelloPage(self.driver)
