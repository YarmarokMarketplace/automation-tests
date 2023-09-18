class LoginConstants:
    """Stores  constants related to log in form"""

    LOGIN_EMAIL_FIELD_XPATH = './/input[@id="email"]'
    LOGIN_PASSWORD_FIELD_XPATH = './/input[@id="password"]'
    LOGIN_BUTTON_XPATH = './/button[@id="login-btn"]'

    SAVE_DATA_FOR_LOGIN_CHECKBOX = './/input[@class="PrivateSwitchBase-input css-1m9pwf3"]'

    SIGN_UP_BUTTON_IN_LOGIN_XPATH = './/button[@id="register-redirect"]'

    USERNAME_IN_THE_HEADER_XPATH = './/button[@id="acc-text-btn"]'

    FORGET_PASSWORD_BUTTON = './/p[@class="css-t1jlua"]'
    RESET_PASSWORD_HEADER_XPATH = './/h4[@class="MuiTypography-root MuiTypography-h4 css-dpr514-MuiTypography-root"]'
    RESET_PASSWORD_HEADER_TEXT = 'Відновлення паролю'

    EMAIL_ERROR_MESSAGE_XPATH = './/p[@id="email-helper-text"]'
    PSW_ERROR_MESSAGE_XPATH = './/p[@id="password-helper-text"]'
    EMAIL_EMPT_ERROR_MESSAGE_TEXT = 'Не забудьте ввести ваш email'
    PSW_EMPT_ERROR_MESSAGE_TEXT = 'Не забудьте ввести пароль'

    ERROR_WITHOURT_REGISTRATION_TEXT = 'Email або пароль невірні'
