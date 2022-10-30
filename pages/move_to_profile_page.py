from pages.base_page import BasePage
from locators.navigate_locators.header_navigate_locators import HeaderNavigateLocators


class MoveToProfilePage(BasePage):

    def move_to_profile(self):
        self.element_is_visible(HeaderNavigateLocators.DROPDOWN_MENU).click()
        self.element_is_visible(HeaderNavigateLocators.MY_PROFILE).click()
        # перенести
        self.element_to_be_clickable(HeaderNavigateLocators.PROFILE_OPTION).click()

