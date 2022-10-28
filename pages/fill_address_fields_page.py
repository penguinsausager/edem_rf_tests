from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.create_trip_related_locators.address_fields_locators import FillAddressFieldsLocators
from locators.navigate_locators.header_navigate_locators import NavigateLocators
from locators.submit_button_locator import SubmitButtonLocator


class FillAddressFields(BasePage):
    def fill_address_fields_and_submit(self):
        # Переход на страницу создания поездки
        self.element_is_visible(NavigateLocators.CREATE_TRIP_BUTTON).click()

        # Ввод значений в поля "Откуда" и "Улица, район отправления"
        self.element_is_visible(FillAddressFieldsLocators.CITY_FROM).send_keys('Екатеринбург')
        self.element_to_be_clickable(FillAddressFieldsLocators.DROPDOWN_WINDOW_CITY_FROM)
        self.element_is_visible(FillAddressFieldsLocators.CITY_FROM).send_keys(Keys.ENTER)
        self.element_is_visible(FillAddressFieldsLocators.FROM_ADDRESS).send_keys('Южный автовокзал')

        # Ввод значения в поля "Куда" и "Улица, район прибытия"
        self.element_is_visible(FillAddressFieldsLocators.TO_CITY).send_keys('Пермь')
        self.element_to_be_clickable(FillAddressFieldsLocators.DROPDOWN_WINDOW_TO_CITY)
        self.element_is_visible(FillAddressFieldsLocators.TO_CITY).send_keys(Keys.ENTER)
        self.element_is_visible(FillAddressFieldsLocators.TO_ADDRESS).send_keys('Ленина 28')

        # Нажатие на клавишу "Далее"
        self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON).click()
