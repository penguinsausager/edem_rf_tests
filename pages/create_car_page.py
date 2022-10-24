from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.create_car_locators import CreateCarLocators
from locators.submit_button_locator import SubmitButtonLocator


class CreateCarPage(BasePage):

    def create_car_and_submit(self):
        self.element_to_be_clickable(CreateCarLocators.CAR_BRAND_INPUT).send_keys('Toyota')
        self.element_to_be_clickable(CreateCarLocators.CAR_BRAND_INPUT).send_keys(Keys.ENTER)
        self.element_to_be_clickable(CreateCarLocators.CAR_MODEL_INPUT).send_keys('Supra')
        self.element_to_be_clickable(CreateCarLocators.CAR_MODEL_INPUT).send_keys(Keys.ENTER)
        self.element_to_be_clickable(CreateCarLocators.CAR_YEAR).send_keys('1998')
        self.element_to_be_clickable(CreateCarLocators.CAR_COLOR).click()
        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()