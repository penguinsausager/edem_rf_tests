from locators.navigate_locators.header_navigate_locators import NavigateLocators
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.submit_button_locator import SubmitButtonLocator
from auth_data import phone_number, password
import time


class LoginPage(BasePage):

    def fill_fields_and_submit(self):
        self.element_is_visible(NavigateLocators.LOGIN_BUTTON).click()

        # закомментить после загрузки куки
        # self.element_is_visible(LoginPageLocators.PHONE_NUMBER_INPUT).send_keys(phone_number)
        # self.element_is_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        # time.sleep(1)
        # self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON).click()
        # time.sleep(1)
