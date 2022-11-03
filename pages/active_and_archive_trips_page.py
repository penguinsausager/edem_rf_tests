from pages.base_page import BasePage
from locators.body_locators.edit_and_delete_trips.active_and_archive_trips_locators import ActiveAndArchiveTripsLocators


class ActiveAndArchiveTripsPage(BasePage):

    def trip_details_click(self):
        self.element_to_be_clickable(ActiveAndArchiveTripsLocators.TRIP_DETAILS).click()
