from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.profile_locators.car_locators import CarLocators
from locators.submit_button_locator import SubmitButtonLocator


class CarPage(BasePage):

    def create_car_and_submit(self):
        self.element_to_be_clickable(CarLocators.CAR_BRAND_INPUT).send_keys('Toyota')
        self.element_to_be_clickable(CarLocators.CAR_BRAND_INPUT).send_keys(Keys.ENTER)
        self.element_to_be_clickable(CarLocators.CAR_MODEL_INPUT).send_keys('Supra')
        self.element_to_be_clickable(CarLocators.CAR_MODEL_INPUT).send_keys(Keys.ENTER)
        self.element_to_be_clickable(CarLocators.CAR_YEAR).send_keys('1998')
        self.element_to_be_clickable(CarLocators.CAR_COLOR).click()
        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()

    def delete_car_and_submit(self):
        self.element_to_be_clickable(CarLocators.SELECT_CAR_FIRST).click()
        self.element_to_be_clickable(CarLocators.DELETE_CAR).click()
        self.element_to_be_clickable(CarLocators.DELETE_CONFIRM).click()
