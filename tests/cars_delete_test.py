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

        profile_options = MainProfilePage(driver)
        cars = CarEditPage(driver)
        personal_data = PersonalDataPage(driver)

        profile_options.move_to_profile_options()
        personal_data.move_to_auto()
        try:
            while cars.cars_count() != 0:
                current_cars_count = cars.cars_count()
                cars.delete_car_and_submit()
                cars_count_after_delete = cars.cars_count()
                assert cars_count_after_delete == current_cars_count - 1
            else:
                cars.delete_car_and_submit()
                cars_count_after_delete = cars.cars_count()
                assert cars_count_after_delete == cars.cars_count()
        except TimeoutException:
            print('NO CARS TO DELETE')
