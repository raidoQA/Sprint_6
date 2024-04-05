from selenium.webdriver.common.by import By

class OrderPageLocators:
    
    # Данные для заполнения в разделе "Для кого самокат"
    name_input = [By.XPATH, "//input[@placeholder='* Имя']"] # ввод имени
    surname_input = [By.XPATH, "//input[@placeholder='* Фамилия']"] # ввод фамилии
    address_input = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"] # ввод адреса доставки
    metro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    metro1 = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='Чистые пруды']")
    metro2 = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='Охотный Ряд']")
    phonenumber_input = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"] # ввод номера телефона
    button_next = [By.XPATH, "//button[text()='Далее']"] # кнопка "Далее"

    # Данные для заполнения в разделе "Про аренду" после перехода по кнопке "Далее"
    calendar = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"] # поле дата
    date_first = [By.XPATH, "//div[@aria-label = 'Choose вторник, 9-е апреля 2024 г.']"] # выбор даты
    date_second = [By.XPATH, "//div[@aria-label = 'Choose среда, 10-е апреля 2024 г.']"] # выбор даты
    rent = [By.XPATH, ".//span[@class = 'Dropdown-arrow']"] # поле аренда
    rental_period_1 = [By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"] # срок аренды
    rental_period_2 = [By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']"] # срок аренды
    color_black = [By.ID, "black"] # выбор черный жемчуг
    color_gray = [By.ID, "grey"] # выбор серая безысходность
    comment_for_courier = [By.XPATH, './/input[@placeholder = "Комментарий для курьера"]'] # коммент для курьера
    order_button = [By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/button[text()='Заказать']"] # кнопка "Заказать"
    yes_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"] # кнопка "Да"
    no_button = [By.XPATH, "//button[contains(text(),'Нет')]"] # кнопка "Нет"
    status = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"] # статус заказа