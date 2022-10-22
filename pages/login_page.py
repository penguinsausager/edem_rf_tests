import time

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.submit_button_locator import SubmitButtonLocator
from login_data import LoginData


class LoginPage(BasePage):

    def fill_fields_and_submit(self):
        self.element_is_visible(LoginPageLocators.LOGIN_BUTTON).click()
        self.element_is_visible(LoginPageLocators.PHONE_NUMBER_INPUT).send_keys(LoginData.phone_number)
        self.element_is_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(LoginData.password)
        time.sleep(10)
        self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON).click()
        time.sleep(5)
