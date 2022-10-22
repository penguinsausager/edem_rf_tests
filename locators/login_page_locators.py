from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.header_auth-box_sign :nth-child(2)')
    PHONE_NUMBER_INPUT = (By.XPATH, '//input[@name="phone"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')