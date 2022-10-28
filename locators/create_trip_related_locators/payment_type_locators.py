from selenium.webdriver.common.by import By

"""Чекбоксы для выбора способа оплаты"""


class PaymentTypeLocators:

    PAYMENT_TYPE_CASH_OR_CARD = (By.XPATH, '(//div[@class="ways-middle_text-primary"])[1]')
    PAYMENT_TYPE_CARD = (By.XPATH, '(//div[@class="ways-middle_text-primary"])[2]')
    PAYMENT_TYPE_CASH = (By.XPATH, '(//div[@class="ways-middle_text-primary"])[3]')
