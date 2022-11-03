from pages.base_page import BasePage
from locators.submit_button_locator import SubmitButtonLocator


class PaymentConfirmPage(BasePage):

    def confirm_trip_payment(self):
        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()