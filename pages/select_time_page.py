import time

from locators.navigate_locators import NavigateLocators
from pages.base_page import BasePage


class SelectTime(BasePage):

    def select_time_and_submit(self):
        self.element_is_visible(NavigateLocators.LOGIN_BUTTON).click()

