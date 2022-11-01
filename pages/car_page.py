import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.profile_locators.car_locators import CarLocators
from locators.navigate_locators.submit_button_locator import SubmitButtonLocator


class CarPage(BasePage):
    car_brand = 'Toyota'
    car_model = 'Supra'
    car_year = '1998'
    __max_cars_count = 3
    is_car_exist = True

    def __cars_check(self):
        return len(self.elements_are_visible(CarLocators.SELECT_ALL_CARS))

    def __create_car(self):
        self.element_to_be_clickable(CarLocators.CAR_BRAND_INPUT).send_keys(self.car_brand)
        self.element_to_be_clickable(CarLocators.CAR_BRAND_INPUT).send_keys(Keys.ENTER)
        self.element_to_be_clickable(CarLocators.CAR_MODEL_INPUT).send_keys(self.car_model)
        self.element_to_be_clickable(CarLocators.CAR_MODEL_INPUT).send_keys(Keys.ENTER)
        self.element_to_be_clickable(CarLocators.CAR_YEAR).send_keys(self.car_year)
        self.element_to_be_clickable(CarLocators.CAR_COLOR).click()

    def create_car_and_submit(self):
        if self.__cars_check != self.__max_cars_count:
            self.element_to_be_clickable(CarLocators.CREATE_CAR_BUTTON).click()
            self.__create_car()
            self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON_ON_CREATE_ROUTE_CAR).click()
            self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON)
            self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON)
            self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()
            self.is_car_exist = False
        # elif self.__cars_check == self.__max_cars_count:
        #     self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()
        #     self.is_car_exist = False
        elif self.is_car_exist:
            self.__create_car()
            self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()

    def delete_car_and_submit(self):
        self.element_to_be_clickable(CarLocators.SELECT_CAR_FIRST).click()
        self.element_to_be_clickable(CarLocators.DELETE_CAR).click()
        self.element_to_be_clickable(CarLocators.DELETE_CONFIRM).click()
