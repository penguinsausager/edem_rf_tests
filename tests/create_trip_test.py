import time
import pytest
from pages.date_page import DatePage
from pages.car_edit_page import CarEditPage
from pages.trip_details_page import TripDetailsPage
from pages.trip_cost_page import TripCostPage
from pages.payment_type_page import PaymentTypePage
from pages.payment_confirm_page import PaymentConfirmPage
from pages.promo_page import PromoPage
from config import base_url, auth
from pages.address_fields_page import AddressFieldsPage


@pytest.mark.order3
class TestCreateTrip:

    def test_fill_address(self, driver):
        auth(driver)
        address_fields_page = AddressFieldsPage(driver)
        address_fields_page.fill_address_fields_and_submit()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/create-route/date', 'URLS ARE NOT THE SAME'

    def test_select_date(self, driver):
        date_page = DatePage(driver)
        date_page.select_date_and_submit()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/create-route/car', 'URLS ARE NOT THE SAME'

    def test_create_car(self, driver):
        car_edit_page = CarEditPage(driver)
        car_edit_page.create_car_and_submit()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/create-route/details', 'URLS ARE NOT THE SAME'

    def test_trip_details(self, driver):
        trip_details_page = TripDetailsPage(driver)
        trip_details_page.select_checkboxes_and_submit()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/create-route/costs', 'URLS ARE NOT THE SAME'

    def test_select_trip_cost_and_submit(self, driver):
        trip_costs_page = TripCostPage(driver)
        trip_costs_page.select_cost_checkbox_and_submit()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/create-route/payment-type', 'URLS ARE NOT THE SAME'

    def test_select_payment_type_and_submit(self, driver):
        payment_type_page = PaymentTypePage(driver)
        payment_type_page.select_payment_type_cash()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/create-route/deposit', 'URLS ARE NOT THE SAME'

    def test_payment_confirm(self, driver):
        payment_confirm_page = PaymentConfirmPage(driver)
        payment_confirm_page.confirm_trip_payment()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/create-route/success', 'URLS ARE NOT THE SAME'

    def test_select_promo(self, driver):
        promo_page = PromoPage(driver)
        promo_page.select_free_promo()
        time.sleep(1)
        assert driver.current_url == f'{base_url()}/account/routes', 'URLS ARE NOT THE SAME'

