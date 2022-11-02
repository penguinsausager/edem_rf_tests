from pages.base_page import BasePage
from locators.navigate_locators.submit_button_locators import SubmitButtonLocators


class PaymentConfirmPage(BasePage):

    def confirm_trip_payment(self):
        self.element_to_be_clickable(SubmitButtonLocators.SUBMIT_BUTTON).click()