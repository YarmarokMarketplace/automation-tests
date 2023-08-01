class HomePageConstants:
    """Stores  constants related to home page"""

    API_URL = "https://deploy-preview-1--yarmarok-test.netlify.app/"

    CATEGORIES_XPATH = './/h4[@class="MuiTypography-root MuiTypography-h4 css-ob4nwx-MuiTypography-root"]'
    CATEGORIES_TEXT = 'Головні рубрики'

    LOGO_XPATH = './/img[@class="css-8atqhb"]'

    CATEGORY_CAR_IMG_XPATH = './/img[@id="category-db74"]'
    CATEGORY_BUSINESS_IMG_XPATH = './/img[@id="category-db75"]'
    CATEGORY_FOR_FREE_IMG_XPATH = './/img[@id="category-db76"]'
    CATEGORY_CHILDREN_WORLD_IMG_XPATH = './/img[@id="category-db77"]'
    CATEGORY_HOME_IMG_XPATH = './/img[@id="category-db78"]'
    CATEGORY_HELP_IMG_XPATH = './/img[@id="category-db79"]'
    CATEGORY_ELECTRO_IMG_XPATH = './/img[@id="category-db7a"]'
    CATEGORY_TRANSPORT_IMG_XPATH = './/img[@id="category-db7b"]'
    CATEGORY_FASHION_IMG_XPATH = './/img[@id="category-db7c"]'
    CATEGORY_PROPERTY_IMG_XPATH = './/img[@id="category-db7d"]'
    CATEGORY_EXCHANGE_IMG_XPATH = './/img[@id="category-db7e"]'
    CATEGORY_REPAIR_IMG_XPATH = './/img[@id="category-db7f"]'
    CATEGORY_WORK_IMG_XPATH = './/img[@id="category-db80"]'
    CATEGORY_PETS_IMG_XPATH = './/img[@id="category-db81"]'
    CATEGORY_VICTORY_IMG_XPATH = './/img[@id="category-db82"]'
    CATEGORY_RELAX_IMG_XPATH = './/img[@id="category-db83"]'

    CATEGORY_CAR_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Авто"]'
    CATEGORY_BUSINESS_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Бізнес та послуги"]'
    CATEGORY_FOR_FREE_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Безкоштовно"]'
    CATEGORY_CHILDREN_WORLD_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Дитячий світ"]'
    CATEGORY_HOME_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Дім і сад"]'
    CATEGORY_HELP_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Допомога"]'
    CATEGORY_ELECTRO_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Електроніка"]'
    CATEGORY_TRANSPORT_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Запчастини для транспорту"]'
    CATEGORY_FASHION_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Мода і стиль"]'
    CATEGORY_PROPERTY_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Нерухомість"]'
    CATEGORY_EXCHANGE_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Обмін"]'
    CATEGORY_REPAIR_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Ремонт"]'
    CATEGORY_WORK_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Робота"]'
    CATEGORY_PETS_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Тварини"]'
    CATEGORY_VICTORY_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Товари для перемоги"]'
    CATEGORY_RELAX_TITLE_XPATH = './/a[@class="css-puq1qr" and text()="Хобі, відпочинок і спорт"]'

    CATEGORY_CAR_TITLE_TEXT = "Авто"
    CATEGORY_BUSINESS_TITLE_TEXT = "Бізнес та послуги"
    CATEGORY_FOR_FREE_TITLE_TEXT = "Безкоштовно"
    CATEGORY_CHILDREN_WORLD_TITLE_TEXT = "Дитячий світ"
    CATEGORY_HOME_TITLE_TEXT = "Дім і сад"
    CATEGORY_HELP_TITLE_TEXT = "Допомога"
    CATEGORY_ELECTRO_TITLE_TEXT = 'Електроніка'
    CATEGORY_TRANSPORT_TITLE_TEXT = "Запчастини для транспорту"
    CATEGORY_FASHION_TITLE_TEXT = "Мода і стиль"
    CATEGORY_PROPERTY_TITLE_TEXT = "Нерухомість"
    CATEGORY_EXCHANGE_TITLE_TEXT = "Обмін"
    CATEGORY_REPAIR_TITLE_TEXT = "Ремонт"
    CATEGORY_WORK_TITLE_TEXT = "Робота"
    CATEGORY_PETS_TITLE_TEXT = "Тварини"
    CATEGORY_VICTORY_TITLE_TEXT = "Товари для перемоги"
    CATEGORY_RELAX_TITLE_TEXT = 'Хобі, відпочинок і спорт'

    # CATEGORY_ALL_TITLE_XPATH = './/a[@class="css-9zxssz" and text()="Переглянути всі"]'

    HEADER_XPATH = './/header'

    FOOTER_XPATH = './/footer'

    TERMS_OF_USE_UKR_XPATH = './/a[@class="MuiTypography-root MuiTypography-inherit MuiLink-root ' \
                             'MuiLink-underlineAlways css-jsb67t-MuiTypography-root-MuiLink-root"][1] '
    TERMS_OF_USE_UKR_TEXT = 'Умови використання'

    SECURITY_POLICY_UKR_XPATH = './/a[@class="MuiTypography-root MuiTypography-inherit MuiLink-root ' \
                                'MuiLink-underlineAlways css-jsb67t-MuiTypography-root-MuiLink-root"][3] '
    SECURITY_POLICY_UKR_TEXT = 'Правила безпеки'

    SITE_MAP_UKR_XPATH = './/a[@class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways ' \
                         'css-jsb67t-MuiTypography-root-MuiLink-root"][4] '
    SITE_MAP_UKR_TEXT = 'Карта сайту'

    HOW_TO_SELL_AND_BUY_UKR_XPATH = './/a[@class="MuiTypography-root MuiTypography-inherit MuiLink-root ' \
                                    'MuiLink-underlineAlways css-jsb67t-MuiTypography-root-MuiLink-root"][2] '
    HOW_TO_SELL_AND_BUY_UKR_TEXT = 'Як продавати й купувати?'
