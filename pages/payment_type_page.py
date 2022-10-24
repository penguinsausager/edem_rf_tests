import time

from pages.base_page import BasePage
from locators.select_date_locators import SelectDateLocators
from locators.submit_button_locator import SubmitButtonLocator
from locators.payment_type_locators import PaymentTypeLocators


class PaymentTypePage(BasePage):

    def select_payment_type(self):
        self.element_to_be_clickable(PaymentTypeLocators.PAYMENT_TYPE).click()
        self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON).click()
