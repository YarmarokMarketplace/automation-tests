class SingleProductPageConst:
    """Stores  constants related to single product page"""

    CREATE_TITLE_INPUT_XPATH = './/input[@name="title"]'
    CREATE_TITLE_ERROR_XPATH = './/h6[@id="title-error"]'
    CREATE_TITLE_ERROR_TEXT = 'Не забудьте ввести назву'

    CREATE_DESCR_INPUT_XPATH = '//textarea[@id=":r18:"]'
    CREATE_DESCR_ERROR_XPATH = './/h6[@id="description-error"]'
    CREATE_DESCR_ERROR_TEXT = 'Не забудьте додати опис'

    SELECT_CATEGORY_XPATH = '//div[@id="select-category"]'
    AUTO_NOTICE_CATEGORY_XPATH = '//li[@data-value="auto"]'
    BUSINESS_NOTICE_CATEGORY_XPATH = '//li[@data-value="business-and-services"]'
    FREE_NOTICE_CATEGORY_XPATH = '//li[@data-value="for-free"]'
    CHILDREN_WORLD_NOTICE_CATEGORY_XPATH = '//li[@id="649760e48aa29bef3c62db77"]'
    HOME_NOTICE_CATEGORY_XPATH = '//li[@data-value="home-and-garden"]'
    HELP_NOTICE_CATEGORY_XPATH = '//li[@data-value="help"]'
    ELECTRONICS_NOTICE_CATEGORY_XPATH = '//li[@data-value="electronics"]'
    PARTS_TRANSPORT_NOTICE_CATEGORY_XPATH = '//li[@data-value="spare-parts-for-transport"]'
    FASHION_NOTICE_CATEGORY_XPATH = '//li[@data-value="fashion-and-style"]'
    REALTY_NOTICE_CATEGORY_XPATH = '//li[@data-value="realty"]'
    EXCHANGE_NOTICE_CATEGORY_XPATH = '//li[@data-value="exchange"]'
    REPAIR_NOTICE_CATEGORY_XPATH = '//li[@data-value="repair"]'
    WORK_NOTICE_CATEGORY_XPATH = '//li[@data-value="work"]'
    PET_NOTICE_CATEGORY_XPATH = '//li[@data-value="animal"]'
    WIN_NOTICE_CATEGORY_XPATH = '//li[@data-value="goods-to-win"]'
    HOBBY_NOTICE_CATEGORY_XPATH = '//li[@data-value="hobbies-recreation-sports"]'

    CATEGORY_ERROR_XPATH = './/h6[@id="category-error"]'
    CATEGORY_ERROR_TEXT = 'Не забудьте обрати категорію'

    PRICE_NOTICE_INPUT_XPATH = './/input[@id=":r2:"]'
    PRICE_ERROR_XPATH = './/h6[@id="price-error"]'
    PRICE_ERROR_TEXT = 'Не забудьте вказати ціну'

    GOODTYPE_RADIOBUTTON_XPATH = '//label[@id="new"]'

    CONTACT_NAME_INPUT_XPATH = './/input[@name="contactName"]'
    CONTACT_NAME_ERROR_XPATH = './/h6[@id="contactName-error"]'
    CONTACT_NAME_ERROR_TEXT = 'Не забудьте ввести ваше ім’я'

    PHONE_INPUT_XPATH = './/input[@id=":r4:"]'
    PHONE_ERROR_XPATH = './/h6[@id="contactNumber-error"]'
    PHONE_ERROR_TEXT = 'Невірний формат номеру'

    LOCATION_KYIV = '//li[@id="Kyiv"]'
    LOCATION_DNIPRO = '//li[@id="Dnipro"]'
    LOCATION_KHARKIV = '//li[@id="Kharkiv"]'
    LOCATION_ODESA = '//li[@id="Odesa"]'
    LOCATION_LVIV = '//li[@id="Lviv"]'
    LOCATION_KHERSON = '//li[@id="Kherson"]'

    POLITIC_AGREE_CHECKBOX_XPATH = './/input[@name="agree"]'
    POLITIC_AGREE_ERROR_XPATH = './/h6[@id="terms-error"]'
    POLITIC_AGREE_ERROR_TEXT = 'Ви маєте погодитися з Політикою конфіденційності'

    POSTED_BUTTON_XPATH = './/button[@id="submit-btn"]'
