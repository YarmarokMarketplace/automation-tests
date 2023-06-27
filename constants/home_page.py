class HomePageConstants:
    """Stores  constants related to home page"""

    CATEGORIES_XPATH = './/h4[@class="MuiTypography-root MuiTypography-h4 css-ob4nwx-MuiTypography-root"]'
    CATEGORIES_TEXT = 'Головні рубрики'

    LOGO_XPATH = './/img[@class="css-ufscxh"]'

    CATEGORY_PROPERTY_IMG_XPATH = './/img[@class="css-73nay0"]'
    CATEGORY_PROPERTY_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Нерухомість"]'

    HEADER_XPATH = './/div[@class="MuiToolbar-root MuiToolbar-regular css-1cmqiah-MuiToolbar-root"]'
    FOOTER_XPATH = './/footer'

    TERMS_OF_USE_UKR_XPATH = './/a[@class="MuiTypography-root MuiTypography-inherit MuiLink-root ' \
                             'MuiLink-underlineAlways css-l0mbzj-MuiTypography-root-MuiLink-root"][1] '
    TERMS_OF_USE_UKR_TEXT = 'Умови використання'

    SECURITY_POLICY_UKR_XPATH = './/a[@class="MuiTypography-root MuiTypography-inherit MuiLink-root ' \
                                'MuiLink-underlineAlways css-l0mbzj-MuiTypography-root-MuiLink-root"][3] '
    SECURITY_POLICY_UKR_TEXT = 'Правила безпеки'

    SITE_MAP_UKR_XPATH = './/a[@class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways ' \
                         'css-l0mbzj-MuiTypography-root-MuiLink-root"][4] '
    SITE_MAP_UKR_TEXT = 'Карта сайту'

    HOW_TO_SELL_AND_BUY_UKR_XPATH = './/a[@class="MuiTypography-root MuiTypography-inherit MuiLink-root ' \
                                    'MuiLink-underlineAlways css-l0mbzj-MuiTypography-root-MuiLink-root"][2] '
    HOW_TO_SELL_AND_BUY_UKR_TEXT = 'Як продавати й купувати?'
