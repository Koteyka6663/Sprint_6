from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT_LOCATOR = By.XPATH, "//input[@placeholder='* Имя']"  # Поле ввода имени
    SURNAME_INPUT_LOCATOR = By.XPATH, "//input[@placeholder='* Фамилия']"  # Поле ввода фамилии
    ADDRESS_INPUT_LOCATOR = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # Поле ввода адреса
    STATION_INPUT_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']"  # Поле ввода для выбора станции метро
    STATION_LOCATOR = By.XPATH, "//button[@value='1']"  # Станция метро в выпадашке
    PHONE_INPUT_LOCATOR = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"  # Поле ввода телефона
    NEXT_BUTTON = By.XPATH, "//button[contains(text(),'Далее')]"  # Кнопка "Далее", переход ко второй форме заказа
    DATE_INPUT_LOCATOR = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"  # Поле ввода даты
    BUTTON_NEXT_MONTH_LOCATOR = By.XPATH, "//button[@aria-label='Next Month']"  # Кнопка переключения месяца на следющий
    DAY_INPUT_LOCATOR = By.XPATH, "//div[contains(text(), '14')]"  # День в календаре
    RENT_PERIOD_LOCATOR = By.XPATH, "//div[@class='Dropdown-root']"  # Поле выбора срока  аренды
    PERIOD_LOCATOR = By.XPATH, "//div[contains(text(), 'двое суток')]"  # Период аренды
    COLOR_LOCATOR = By.XPATH, "//input[@id='black']"  # Выбор цвета
    COMMENT_INPUT_LOCATOR = By.XPATH, "//input[@placeholder='Комментарий для курьера']"  # Поле ввода комментария
    ORDER_BUTTON_LOCATOR = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"  # Конапка заказа
    POPUP_BUTTON_YES = By.XPATH, "//button[contains(text(),'Да')]"  # Кнопка подтверждения заказа
    POPUP_BUTTON_STATUS = By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"  # Кнопка перехода к заказу
    LOGO_SCOOTER_LOCATOR = By.XPATH, "//img[@alt='Scooter']"  # Логотип "Самокат"
    LOGO_YANDEX_LOCATOR = By.XPATH, "//img[@alt='Yandex']"  # Логотип "Яндекс"
    DZEN_LOCATOR = By.XPATH, "//a[contains(text(), 'Всё о Дзене')]"  # Жлемент на странице Дзена
