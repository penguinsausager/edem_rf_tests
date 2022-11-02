from selenium.webdriver.common.by import By


class SubmitButtonLocators:
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SUBMIT_BUTTON_ON_CREATE_ROUTE_CAR = (By.XPATH, '(//button[@type="submit"])[2]')