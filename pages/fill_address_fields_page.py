from selenium.webdriver import Keys

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.create_trip_related_locators.address_fields_locators import AddressFieldsLocators
from locators.navigate_locators.header_navigate_locators import HeaderNavigateLocators
from locators.navigate_locators.submit_button_locators import SubmitButtonLocators


class FillAddressFields(BasePage):

    city_from = 'Екатеринбург'
    to_city = 'Пермь'

    def fill_address_fields_and_submit(self):
        # Переход на страницу создания поездки
        self.element_is_visible(HeaderNavigateLocators.CREATE_TRIP_BUTTON).click()

        # Ввод значений в поля "Откуда" и "Улица, район отправления"
        self.element_is_visible(AddressFieldsLocators.CITY_FROM).send_keys(FillAddressFields.city_from)
        self.element_to_be_clickable(AddressFieldsLocators.DROPDOWN_WINDOW_CITY_FROM)
        self.element_is_visible(AddressFieldsLocators.CITY_FROM).send_keys(Keys.ENTER)
        self.element_is_visible(AddressFieldsLocators.FROM_ADDRESS).send_keys('Южный автовокзал')

        # Ввод значения в поля "Куда" и "Улица, район прибытия"
        self.element_is_visible(AddressFieldsLocators.TO_CITY).send_keys(FillAddressFields.to_city)
        self.element_to_be_clickable(AddressFieldsLocators.DROPDOWN_WINDOW_TO_CITY)
        self.element_is_visible(AddressFieldsLocators.TO_CITY).send_keys(Keys.ENTER)
        self.element_is_visible(AddressFieldsLocators.TO_ADDRESS).send_keys('Ленина 28')

        # Нажатие на клавишу "Далее"
        self.element_is_visible(SubmitButtonLocators.SUBMIT_BUTTON).click()
