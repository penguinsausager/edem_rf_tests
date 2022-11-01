import os

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.navigate_locators.submit_button_locator import SubmitButtonLocator
import time


class LoginPage(BasePage):

    def fill_fields_and_submit(self):

        __phone_number = ''
        __password = ''

        if os.getenv('MODE') == 'PROD':
            __phone_number__ = os.getenv('PHONE_NUMBER_PROD')
            __password__ = os.getenv('PASSWORD_PROD')
        elif os.getenv('MODE') == 'BETA':
            __phone_number__ = os.getenv('PHONE_NUMBER_BETA')
            __password__ = os.getenv('PASSWORD_BETA')

        self.element_is_visible(LoginPageLocators.PHONE_NUMBER_INPUT).send_keys(__phone_number)
        self.element_is_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(__password)

        if os.getenv('MODE') == 'PROD':
            time.sleep(10)

        self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON).click()
        time.sleep(1)