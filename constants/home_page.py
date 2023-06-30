class HomePageConstants:
    """Stores  constants related to home page"""

    CATEGORIES_XPATH = './/h4[@class="MuiTypography-root MuiTypography-h4 css-ob4nwx-MuiTypography-root"]'
    CATEGORIES_TEXT = 'Головні рубрики'

    LOGO_XPATH = './/img[@class="css-ufscxh"]'

    CATEGORY_CHILDREN_WORLD_IMG_XPATH = './/img[@class="css-73nay0"]'
    CATEGORY_PROPERTY_IMG_XPATH = './/img[@class="css-73nay0"]'
    CATEGORY_CAR_IMG_XPATH = ''
    CATEGORY_TRANSPORT_IMG_XPATH = ''  # ToDo: add images xpathes when it will be implemented
    CATEGORY_PETS_IMG_XPATH = ''
    CATEGORY_HOME_IMG_XPATH = ''
    CATEGORY_WORK_IMG_XPATH = ''
    CATEGORY_BUSINESS_IMG_XPATH = ''
    CATEGORY_FASHION_IMG_XPATH = ''
    CATEGORY_RELAX_IMG_XPATH = ''
    CATEGORY_ELECTRO_IMG_XPATH = ''

    CATEGORY_CHILDREN_WORLD_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Дитячий світ"]'
    CATEGORY_PROPERTY_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Нерухомість"]'
    CATEGORY_CAR_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Авто"]'
    CATEGORY_TRANSPORT_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Запчастини для транспорту"]'
    CATEGORY_PETS_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Тварини"]'
    CATEGORY_HOME_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Дім і сад"]'
    CATEGORY_WORK_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Робота"]'
    CATEGORY_BUSINESS_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Бізнес та послуги"]'
    CATEGORY_FASHION_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Мода і стиль"]'
    CATEGORY_RELAX_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Хобі, відпочинок і спорт"]'
    CATEGORY_ELECTRO_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Електроніка"]'

    CATEGORY_ALL_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Переглянути всі"]'

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
