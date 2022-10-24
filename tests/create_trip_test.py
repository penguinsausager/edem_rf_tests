import time
import pickle
from auth_data import phone_number
from pages.login_page import LoginPage
from pages.fill_address_fields_page import FillAddressFields
from pages.select_date_page import SelectDate
from pages.create_car_page import CreateCarPage
from pages.trip_details_page import TripDetailsPage
from pages.trip_cost_page import TripCostPage


class TestCreateTrip:

    def test_login(self, driver):
        login_page = LoginPage(driver, 'https://едем.рф')
        login_page.open()
        login_page.fill_fields_and_submit()
        # pickle.dump(driver.get_cookies(), open(f"{phone_number}_cookies", "wb"))
        # driver.delete_all_cookies()
        for cookie in pickle.load(open(f"{phone_number}_cookies", "rb")):
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(1)
        assert driver.current_url == 'https://xn--d1abb2a.xn--p1ai/account/profile', 'URLS ARE NOT THE SAME'

    def test_fill_address(self, driver):
        fill_address_page = FillAddressFields(driver)
        fill_address_page.fill_address_fields_and_submit()
        time.sleep(1)
        assert driver.current_url == 'https://xn--d1abb2a.xn--p1ai/create-route/date', 'URLS ARE NOT THE SAME'

    def test_select_date(self, driver):
        select_date = SelectDate(driver)
        select_date.select_date_and_submit()
        time.sleep(1)
        assert driver.current_url == 'https://xn--d1abb2a.xn--p1ai/create-route/car', 'URLS ARE NOT THE SAME'

    def test_create_car(self, driver):
        create_car = CreateCarPage(driver)
        create_car.create_car_and_submit()
        time.sleep(1)
        assert driver.current_url == 'https://xn--d1abb2a.xn--p1ai/create-route/details', 'URLS ARE NOT THE SAME'

    def test_trip_details(self, driver):
        trip_details = TripDetailsPage(driver)
        trip_details.select_checkboxes()
        time.sleep(1)

    def test_select_trip_cost_and_submit(self, driver):
        trip_costs = TripCostPage(driver)
        trip_costs.select_cost_checkbox_and_submit()
        time.sleep(2)
