import time
import pytest
from config import auth
from pages.header_navigate_page import HeaderNavigatePage


@pytest.mark.skip
class TestTripSearch:

    def test_trip_search(self, driver):
        auth(driver)
        static_page = HeaderNavigatePage(driver)




        static_page.search_trip_click()
        time.sleep(1)
