from pages.base_page import BasePage
from locators.all_routes_locators import AllRoutesLocators


class RoutesPage(BasePage):

    def route_details_click(self):
        self.element_to_be_clickable(AllRoutesLocators.TRIP_DETAILS).click()