from pages.base_page import BasePage
from locators.header_locators.header_navigate_locators import HeaderNavigateLocators


class MainPage(BasePage):

    def login_click(self):
        self.element_is_visible(HeaderNavigateLocators.LOGIN_BUTTON).click()
