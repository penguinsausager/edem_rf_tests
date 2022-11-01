from pages.base_page import BasePage
from locators.navigate_locators.submit_button_locator import SubmitButtonLocator
from locators.create_trip_related_locators.payment_confirm_locators import PaymentConfirmLocators


class PaymentConfirmPage(BasePage):

    def select_payment_type(self):
        self.element_is_visible(PaymentConfirmLocators.CHECKBOX).click()
        self.element_is_visible(PaymentConfirmLocators.CHECKBOX).click()
        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()