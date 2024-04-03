from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка принять куки
    cookie_button = [By.ID, "rcc-confirm-button"]

    # Ссылка на сайт "Самокат"
    scooter_logo_link = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]

    # Ссылка на сайт "Yandex"
    logo_yandex = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]

    # Верхняя кнопка "Заказать"
    header_order_button = [By.XPATH, "//button[@class = 'Button_Button__ra12g']"]

    # Кнопка "Заказать" в середине
    bottom_order_button = [By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/button[text() = 'Заказать']"]

    # Вопросы:
    question_1 = [By.ID, "accordion__heading-0"] # 1-ый вопрос
    question_2 = [By.ID, "accordion__heading-1"] # 2-ой вопрос
    question_3 = [By.ID, "accordion__heading-2"] # 3-ий вопрос
    question_4 = [By.ID, "accordion__heading-3"] # 4-ый вопрос
    question_5 = [By.ID, "accordion__heading-4"] # 5-ый вопрос
    question_6 = [By.ID, "accordion__heading-5"] # 6-ой вопрос
    question_7 = [By.ID, "accordion__heading-6"] # 7-ой вопрос
    question_8 = [By.ID, "accordion__heading-7"] # 8-ой вопрос

    #Ответы:
    answer_1 = [By.ID, "accordion__panel-0"] # 1-ый ответ
    answer_2 = [By.ID, "accordion__panel-1"] # 2-ой ответ
    answer_3 = [By.ID, "accordion__panel-2"] # 3-ий ответ
    answer_4 = [By.ID, "accordion__panel-3"] # 4-ый ответ
    answer_5 = [By.ID, "accordion__panel-4"] # 5-ый ответ
    answer_6 = [By.ID, "accordion__panel-5"] # 6-ой ответ
    answer_7 = [By.ID, "accordion__panel-6"] # 7-ой ответ
    answer_8 = [By.ID, "accordion__panel-7"] # 8-ой ответ