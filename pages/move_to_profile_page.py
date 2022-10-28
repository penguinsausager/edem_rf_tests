from pages.base_page import BasePage
from locators.navigate_locators.header_navigate_locators import NavigateLocators


class MoveToProfilePage(BasePage):

    def move_to_profile(self):
        self.element_is_visible(NavigateLocators.DROPDOWN_MENU).click()
        self.element_is_visible(NavigateLocators.MY_PROFILE).click()
        # перенести
        self.element_to_be_clickable(NavigateLocators.PROFILE_OPTION).click()

