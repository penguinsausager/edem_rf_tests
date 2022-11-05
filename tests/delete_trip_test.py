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
        main_profile_page = MainProfilePage(driver)
        active_and_archive_trips_page = ActiveAndArchiveTripsPage(driver)
        trip_info_page = TripInfoPage(driver)
        edit_trip_page = EditTripPage(driver)

        main_profile_page.activate_dropdown_menu()
        main_profile_page.move_to_trips()
        active_and_archive_trips_page.trip_details_click()
        trip_info_page.edit_trip_click()
        edit_trip_page.edit_and_delete_trip()
        time.sleep(1)
