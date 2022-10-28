from pages.base_page import BasePage
from locators.trip_details_view_locators import TripDetailsViewLocators


class TripDetailsViewPage(BasePage):
    def edit_trip_click(self):
        self.element_to_be_clickable(TripDetailsViewLocators.EDIT_BUTTON).click()
