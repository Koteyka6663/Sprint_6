from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = By.CSS_SELECTOR, ".App_CookieButton__3cvqF"  # Кнопка кук
    QUESTION_LOCATOR = By.XPATH, "//div[@id='accordion__heading-{}']"  # Вопросы
    ANSWER_LOCATOR = By.XPATH, "//div[@id='accordion__panel-{}']"  # Ответы
    BUTTON_ORDER_HEADER = By.XPATH, "//button[@class='Button_Button__ra12g']"  # Кнопка заказа в хедере
    BUTTON_ORDER_ON_PAGE = By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']"  # Кнопка заказа на странице
