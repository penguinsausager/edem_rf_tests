from selenium.common import TimeoutException
from config import auth
from pages.car_page import CarPage
from pages.profile_options_page import AccountProfilePage
from pages.profile_page import ProfileInfoPage


class TestDeleteCar:

    def test_delete_all_cars(self, driver):
        auth(driver)

        profile_options = AccountProfilePage(driver)
        cars = CarPage(driver)
        personal_data = ProfileInfoPage(driver)

        profile_options.move_to_profile_options()
        personal_data.move_to_auto()
        try:
            while cars.cars_count() > 0:
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
