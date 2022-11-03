from pages.base_page import BasePage
from locators.submit_button_locator import SubmitButtonLocator
from locators.body_locators.edit_and_delete_trips.edit_trip_locators import EditTripLocators


class EditTripPage(BasePage):

    def edit_and_delete_trip(self):
        self.element_to_be_clickable(EditTripLocators.DELETE_TRIP).click()
        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()
        