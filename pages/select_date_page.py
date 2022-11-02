import time

from pages.base_page import BasePage
from locators.create_trip_related_locators.date_and_time_locators import DateAndTimeLocators
from locators.navigate_locators.submit_button_locators import SubmitButtonLocators


class SelectDate(BasePage):

    def select_date_and_submit(self):
        self.element_to_be_clickable(DateAndTimeLocators.INPUT_DATE_FIELD).click()
        self.element_to_be_clickable(DateAndTimeLocators.SELECT_NEXT_MONTH_BUTTON).click()
        self.element_to_be_clickable(DateAndTimeLocators.DAY_OF_THE_CURRENT_MONTH).click()

        self.element_to_be_clickable(DateAndTimeLocators.INPUT_TIME_FIELD).click()
        self.element_to_be_clickable(DateAndTimeLocators.HOUR_SELECT).click()
        time.sleep(0.5)
        self.element_to_be_clickable(DateAndTimeLocators.MINUTE_SELECT).click()

        self.element_to_be_clickable(SubmitButtonLocators.SUBMIT_BUTTON).click()
