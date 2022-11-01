from pages.base_page import BasePage
from locators.navigate_locators.submit_button_locator import SubmitButtonLocator


class TripDetailsPage(BasePage):

    def select_checkboxes(self):
        self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON)
        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()
