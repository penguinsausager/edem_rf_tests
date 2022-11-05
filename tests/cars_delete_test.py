import pytest
from selenium.common import TimeoutException
from config import auth
from pages.car_edit_page import CarEditPage
from pages.main_profile_page import MainProfilePage
from pages.personal_data_page import PersonalDataPage


@pytest.mark.order2
class TestDeleteCar:

    def test_delete_all_cars(self, driver):
        auth(driver)

        main_profile_page = MainProfilePage(driver)
        car_edit_page = CarEditPage(driver)
        personal_data_page = PersonalDataPage(driver)

        main_profile_page.move_to_profile_options()
        personal_data_page.move_to_auto()
        try:
            while car_edit_page.cars_count() != 0:
                current_cars_count = car_edit_page.cars_count()
                car_edit_page.delete_car_and_submit()
                cars_count_after_delete = car_edit_page.cars_count()
                assert cars_count_after_delete == current_cars_count - 1
            else:
                car_edit_page.delete_car_and_submit()
                cars_count_after_delete = car_edit_page.cars_count()
                assert cars_count_after_delete == car_edit_page.cars_count()
        except TimeoutException:
            print('NO CARS TO DELETE')
