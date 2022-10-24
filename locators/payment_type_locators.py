from selenium.webdriver.common.by import By


class PaymentTypeLocators:
    PAYMENT_TYPE = (By.XPATH, '(//div[@class="ways-middle_text-primary"])[3]')