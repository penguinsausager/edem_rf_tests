from pages.base_page import BasePage
from locators.navigate_locators.submit_button_locators import SubmitButtonLocators


class TripDetailsPage(BasePage):

    def select_checkboxes_and_submit(self):
        self.element_is_visible(SubmitButtonLocators.SUBMIT_BUTTON)
        self.element_to_be_clickable(SubmitButtonLocators.SUBMIT_BUTTON).click()
