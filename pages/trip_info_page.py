from pages.base_page import BasePage
from locators.body_locators.edit_and_delete_trips.trip_info_locators import TripInfoLocators


class TripInfoPage(BasePage):
    def edit_trip_click(self):
        self.element_to_be_clickable(TripInfoLocators.EDIT_BUTTON).click()
