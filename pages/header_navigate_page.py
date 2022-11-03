from pages.base_page import BasePage
from locators.header_locators.header_navigate_locators import HeaderNavigateLocators


class HeaderNavigatePage(BasePage):

    def search_trip_click(self):
        self.element_to_be_clickable(HeaderNavigateLocators.TRIP_SEARCH).click()

