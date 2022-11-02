from pages.base_page import BasePage
from locators.navigate_locators.submit_button_locators import SubmitButtonLocators


class TripCostPage(BasePage):

    def select_cost_checkbox_and_submit(self):
        self.element_is_visible(SubmitButtonLocators.SUBMIT_BUTTON).click()
