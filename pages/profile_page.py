from pages.base_page import BasePage
from locators.profile_locators.personal_data_locators import PersonalDataLocators


class ProfileInfoPage(BasePage):

    def move_to_auto(self):
        self.element_to_be_clickable(PersonalDataLocators.AUTO).click()
