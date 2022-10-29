from locators.navigate_locators.header_navigate_locators import NavigateLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def login_click(self):
        self.element_is_visible(NavigateLocators.LOGIN_BUTTON).click()
