from selenium.webdriver.common.by import By


class LoginPageLocators:
    PHONE_NUMBER_INPUT = (By.XPATH, '//input[@name="phone"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')