import time

import pytest

from config import auth
from pages.edit_trip_page import EditTripPage
from pages.main_profile_page import MainProfilePage
from pages.active_and_archive_trips_page import ActiveAndArchiveTripsPage
from pages.trip_info_page import TripInfoPage


@pytest.mark.order1
class TestDeleteTrip:

    def test_delete_trip(self, driver):
        auth(driver)
        profile_options = MainProfilePage(driver)
        trip_details = ActiveAndArchiveTripsPage(driver)
        edit_trip_button_click = TripInfoPage(driver)
        edit_trip_page = EditTripPage(driver)

        profile_options.activate_dropdown_menu()
        profile_options.move_to_trips()
        trip_details.trip_details_click()
        edit_trip_button_click.edit_trip_click()
        edit_trip_page.edit_and_delete_trip()
        time.sleep(1)
