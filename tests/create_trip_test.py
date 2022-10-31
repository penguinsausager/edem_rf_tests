import time
import os.path
from pages.login_page import LoginPage
from pages.fill_address_fields_page import FillAddressFields
from pages.select_date_page import SelectDate
from pages.car_page import CarPage
from pages.trip_details_page import TripDetailsPage
from pages.trip_cost_page import TripCostPage
from pages.payment_type_page import PaymentTypePage
from pages.payment_confirm_page import PaymentConfirmPage
from pages.routes_page import RoutesPage
from pages.select_promo_page import SelectPromoPage
from pages.trip_details_view_page import TripDetailsViewPage
from pages.edit_trip_page import EditTrip
from pages.move_to_profile_page import MoveToProfilePage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from config import base_url, auth, base_auth_url
from login_test import TestLogin


class TestCreateTrip:

    def test_fill_address(self, driver):
        auth(driver)
        fill_address_page = FillAddressFields(driver)
        fill_address_page.fill_address_fields_and_submit()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/create-route/date', 'URLS ARE NOT THE SAME'

    def test_select_date(self, driver):
        select_date = SelectDate(driver)
        select_date.select_date_and_submit()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/create-route/car', 'URLS ARE NOT THE SAME'

    def test_create_car(self, driver):
        create_car = CarPage(driver)
        create_car.create_car_and_submit()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/create-route/details', 'URLS ARE NOT THE SAME'

    def test_trip_details(self, driver):
        trip_details = TripDetailsPage(driver)
        trip_details.select_checkboxes()
        time.sleep(1)

    def test_select_trip_cost_and_submit(self, driver):
        trip_costs = TripCostPage(driver)
        trip_costs.select_cost_checkbox_and_submit()
        time.sleep(1)

    def test_select_payment_type_and_submit(self, driver):
        select_payment_type = PaymentTypePage(driver)
        select_payment_type.select_payment_type()
        time.sleep(1)

    def test_payment_confirm(self, driver):
        payment_confirm = PaymentConfirmPage(driver)
        payment_confirm.select_payment_type()
        time.sleep(1)

    def test_select_promo(self, driver):
        select_promo = SelectPromoPage(driver)
        select_promo.select_promo()
        time.sleep(1)

    def test_route_details(self, driver):
        trip_details = RoutesPage(driver)
        trip_details.route_details_click()
        time.sleep(1)

    def test_click_edit_trip_button(self, driver):
        edit_trip_button_click = TripDetailsViewPage(driver)
        edit_trip_button_click.edit_trip_click()
        time.sleep(1)

    def test_edit_and_delete_trip(self, driver):
        edit_and_delete_trip = EditTrip(driver)
        edit_and_delete_trip.edit_and_delete_trip()
        time.sleep(1)

    def test_move_to_profile(self, driver):
        move_to_profile = MoveToProfilePage(driver)
        move_to_profile.move_to_profile()
        time.sleep(1)

    def test_move_to_auto_edit(self, driver):
        move_to_auto = ProfilePage(driver)
        move_to_auto.move_to_auto()
        time.sleep(1)

    def test_delete_car(self, driver):
        delete_car_and_submit = CarPage(driver)
        delete_car_and_submit.delete_car_and_submit()
        time.sleep(2)


