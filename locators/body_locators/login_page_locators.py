from selenium.webdriver.common.by import By

"""Локаторы на странице входа"""


class LoginPageLocators:
    PHONE_NUMBER_INPUT = (By.XPATH, '//input[@name="phone"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')

    RESET_PASSWORD = (By.CSS_SELECTOR, '.form-group_icon-theme')

    REGISTER_BUTTON = (By.XPATH, '//div[@class = "common_form-footer-cell"]')
    REMIND_PASS_BUTTON = (By.XPATH, '//div[@class = "common_form-footer-cell"][2]')
