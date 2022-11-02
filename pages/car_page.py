import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.profile_locators.car_locators import CarLocators
from locators.navigate_locators.submit_button_locator import SubmitButtonLocator


class CarPage(BasePage):
    car_brand = 'Toyota'
    car_model = 'Supra'
    car_year = '1998'
    __max_cars_count = 3

    def cars_count(self):
        if not self.presence_of_element_located(CarLocators.SELECT_ALL_CARS):
            return 0
        return len(self.elements_are_visible(CarLocators.SELECT_ALL_CARS))

    def create_car_and_submit(self):
        self.element_to_be_clickable(CarLocators.CAR_BRAND_INPUT).send_keys(self.car_brand)
        self.element_to_be_clickable(CarLocators.CAR_BRAND_INPUT).send_keys(Keys.ENTER)
        self.element_to_be_clickable(CarLocators.CAR_MODEL_INPUT).send_keys(self.car_model)
        self.element_to_be_clickable(CarLocators.CAR_MODEL_INPUT).send_keys(Keys.ENTER)
        self.element_to_be_clickable(CarLocators.CAR_YEAR).send_keys(self.car_year)
        self.element_to_be_clickable(CarLocators.CAR_COLOR).click()
        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()

    def delete_car_and_submit(self):
        self.element_to_be_clickable(CarLocators.SELECT_CAR_FIRST).click()
        self.element_to_be_clickable(CarLocators.DELETE_CAR).click()
        self.element_to_be_clickable(CarLocators.DELETE_CONFIRM).click()
