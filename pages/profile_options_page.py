from locators.navigate_locators.header_navigate_locators import HeaderNavigateLocators
from pages.base_page import BasePage
from locators.navigate_locators.submit_button_locator import SubmitButtonLocator
from locators.create_trip_related_locators.payment_type_locators import PaymentTypeLocators

""""Страница "Мой профиль" """


class AccountProfilePage(BasePage):

    def move_to_profile_options(self):
        self.element_to_be_clickable(HeaderNavigateLocators.PROFILE_OPTION).click()

    def activate_dropdown_menu(self):
        self.element_to_be_clickable(HeaderNavigateLocators.DROPDOWN_MENU).click()

    def move_to_trips(self):
        self.element_to_be_clickable(HeaderNavigateLocators.DRIVER).click()
