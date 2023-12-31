class RegistrationConstants:
    """Stores  constants related to registration"""

    SIGN_UP_USERNAME_FIELD_XPATH = './/input[@id="name"]'
    SIGN_UP_EMAIL_FIELD_XPATH = './/input[@id="email"]'
    SIGN_UP_PASSWORD_FIELD_XPATH = './/input[@id="password"]'
    SIGN_UP_CONFIRM_PASSWORD_FIELD_XPATH = './/input[@id="confirmPassword"]'

    SIGN_UP_BUTTON_XPATH = './/button[@id="register-btn"]'

    TERMS_OF_USE_XPATH = './/a[@id="rules-link"]'
    LOGIN_BUTTON_IN_REGFORM_XPATH = './/button[@id="login-redirect"]'

    TEXT_AFTER_REGISTR_XPATH = './/p[@class="MuiTypography-root MuiTypography-body1 css-16nfqyq-MuiTypography-root"]'
    TEXT_AFTER_REGISTRATION_TEXT = 'Дякуємо за реєстрацію!'

    NAME_ERROR_MESSAGE_XPATH = './/p[@id="name-helper-text"]'
    EMAIL_ERROR_MESSAGE_XPATH = './/p[@id="email-helper-text"]'
    PSW_ERROR_MESSAGE_XPATH = './/p[@id="password-helper-text"]'
    CONFIRM_PSW_ERROR_MESSAGE_XPATH = './/p[@id="confirmPassword-helper-text"]'

    EMPTY_NAME_ERROR_MESSAGE_TEXT = 'Не забудьте ввести ваше ім’я'
    SHORT_NAME_ERROR_MESSAGE_TEXT = 'Мінімальна довжина 2 символи'

    EMAIL_ERROR_MESSAGE_TEXT = 'Некоректна електронна адреса. Перевірте правильність введення електронної адреси.'
    DUPLICATE_EMAIL_ERROR_MESSAGE_TEXT = 'Користувач з такою поштою вже зареєстрований'

    EMPTY_PSW_ERROR_MESSAGE_TEXT = 'Не забудьте ввести пароль'
    SHORT_PSW_ERROR_MESSAGE_TEXT = 'Пароль повинен мати мінімум 8 символів'
    INV_PSW_ERROR_TEXT = 'Пароль має містити лише латинські літери, хоча б одну велику літеру, одну цифру та ' \
                         'спеціальний символ (#._?!@$%^&*-)'

    INVALID_CONFIRM_PSW_ERROR_MESSAGE_TEXT = 'Введені паролі не збігаються.'

    CLOSE_REGISTRATION_FORM_BUTTON_XPATH = './/button[@class="MuiButtonBase-root MuiIconButton-root ' \
                                           'MuiIconButton-colorInherit MuiIconButton-sizeMedium ' \
                                           'css-xdwiov-MuiButtonBase-root-MuiIconButton-root"] '
