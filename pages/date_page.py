import time
from pages.base_page import BasePage
from locators.submit_button_locator import SubmitButtonLocator
from locators.body_locators.create_trip_locators.date_and_time_locators import DateAndTimeLocators


class DatePage(BasePage):

    def select_date_and_submit(self):
        self.element_to_be_clickable(DateAndTimeLocators.INPUT_DATE_FIELD).click()
        self.element_to_be_clickable(DateAndTimeLocators.SELECT_NEXT_MONTH_BUTTON).click()
        self.element_to_be_clickable(DateAndTimeLocators.DAY_OF_THE_CURRENT_MONTH).click()

        self.element_to_be_clickable(DateAndTimeLocators.INPUT_TIME_FIELD).click()
        self.element_to_be_clickable(DateAndTimeLocators.HOUR_SELECT).click()
        time.sleep(0.5)
        self.element_to_be_clickable(DateAndTimeLocators.MINUTE_SELECT).click()

        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()
