from pages.base_page import BasePage
from locators.submit_button_locator import SubmitButtonLocator


class TripCostPage(BasePage):

    def select_cost_checkbox_and_submit(self):
        self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON).click()
