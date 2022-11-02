import time
from config import base_url, auth
from pages.edit_trip_page import EditTrip
from pages.fill_address_fields_page import FillAddressFields
from pages.profile_options_page import AccountProfilePage
from pages.routes_page import RoutesPage
from pages.trip_details_view_page import TripDetailsViewPage


class TestDeleteTrip:

    def test_delete_trip(self, driver):
        auth(driver)
        profile_options = AccountProfilePage(driver)
        profile_options.activate_dropdown_menu()
        profile_options.move_to_trips()

        trip_details = RoutesPage(driver)
        trip_details.trip_details_click()

        edit_trip_button_click = TripDetailsViewPage(driver)
        edit_trip_button_click.edit_trip_click()

        edit_and_delete_trip = EditTrip(driver)
        edit_and_delete_trip.edit_and_delete_trip()
        time.sleep(2)

