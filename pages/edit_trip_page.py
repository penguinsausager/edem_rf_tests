from pages.base_page import BasePage
from locators.navigate_locators.submit_button_locators import SubmitButtonLocators
from locators.edit_trip_locators import EditTripLocators


class EditTrip(BasePage):

    def edit_and_delete_trip(self):
        self.element_to_be_clickable(EditTripLocators.DELETE_TRIP).click()
        self.element_to_be_clickable(SubmitButtonLocators.SUBMIT_BUTTON).click()