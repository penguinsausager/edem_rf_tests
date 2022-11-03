from locators.header_locators.header_navigate_locators import HeaderNavigateLocators
from locators.body_locators.profile_locators.main_profile_locators import MainProfileLocators
from pages.base_page import BasePage


""""Страница "Мой профиль" """


class MainProfilePage(BasePage):

    def move_to_profile_options(self):
        self.element_to_be_clickable(MainProfileLocators.PERSONAL_DATA).click()

    def activate_dropdown_menu(self):
        self.element_to_be_clickable(HeaderNavigateLocators.DROPDOWN_MENU).click()

    def move_to_trips(self):
        self.element_to_be_clickable(HeaderNavigateLocators.DRIVER).click()
