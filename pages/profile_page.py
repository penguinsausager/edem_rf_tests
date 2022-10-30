from pages.base_page import BasePage
from locators.profile_locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):

    def move_to_auto(self):
        self.element_to_be_clickable(ProfileLocators.AUTO).click()
