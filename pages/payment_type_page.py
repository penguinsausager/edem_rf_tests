from pages.base_page import BasePage
from locators.navigate_locators.submit_button_locator import SubmitButtonLocator
from locators.create_trip_related_locators.payment_type_locators import PaymentTypeLocators


class PaymentTypePage(BasePage):

    def select_payment_type_cash(self):
        self.element_to_be_clickable(PaymentTypeLocators.PAYMENT_TYPE_CASH).click()
        self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON).click()