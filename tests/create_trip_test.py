import time
import pickle
from auth_data import phone_number
from pages.login_page import LoginPage
from pages.fill_address_fields_page import FillAddressFields


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
        assert driver.current_url == 'https://xn--d1abb2a.xn--p1ai/account/profile', 'URLS ARE NOT THE SAME'

    def test_fill_address(self, driver):
        fill_address_page = FillAddressFields(driver, 'https://едем.рф/account/profile')
        fill_address_page.open()
        fill_address_page.fill_address_fields_and_submit()
        time.sleep(1)
        assert driver.current_url == 'https://xn--d1abb2a.xn--p1ai/create-route/date', 'URLS ARE NOT THE SAME'
        time.sleep(2)

