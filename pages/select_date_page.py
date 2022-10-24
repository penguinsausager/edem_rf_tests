import time

from pages.base_page import BasePage
from locators.select_date_locators import SelectDateLocators
from locators.submit_button_locator import SubmitButtonLocator


class SelectDate(BasePage):

    def select_date_and_submit(self):
        self.element_to_be_clickable(SelectDateLocators.INPUT_DATE_FIELD).click()
        self.element_to_be_clickable(SelectDateLocators.SELECT_NEXT_MONTH_BUTTON).click()
        self.element_to_be_clickable(SelectDateLocators.DAY_OF_THE_CURRENT_MONTH).click()

        self.element_to_be_clickable(SelectDateLocators.INPUT_TIME_FIELD).click()
        self.element_to_be_clickable(SelectDateLocators.HOUR_SELECT).click()
        time.sleep(0.5)
        self.element_to_be_clickable(SelectDateLocators.MINUTE_SELECT).click()

        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()

