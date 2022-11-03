from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.submit_button_locator import SubmitButtonLocator
from locators.header_locators.header_navigate_locators import HeaderNavigateLocators
from locators.body_locators.create_trip_locators.address_fields_locators import AddressFieldsLocators


class AddressFieldsPage(BasePage):
    city_from = 'Екатеринбург'
    from_address = 'Южный автовокзал'

    to_city = 'Пермь'
    to_address = 'Ленина 28'

    def fill_address_fields_and_submit(self):
        # Переход на страницу создания поездки
        self.element_is_visible(HeaderNavigateLocators.CREATE_TRIP_BUTTON).click()

        # Ввод значений в поля "Откуда" и "Улица, район отправления"
        self.element_is_visible(AddressFieldsLocators.CITY_FROM).send_keys(self.city_from)
        self.element_to_be_clickable(AddressFieldsLocators.DROPDOWN_WINDOW_CITY_FROM)
        self.element_is_visible(AddressFieldsLocators.CITY_FROM).send_keys(Keys.ENTER)
        self.element_is_visible(AddressFieldsLocators.FROM_ADDRESS).send_keys(self.from_address)

        # Ввод значения в поля "Куда" и "Улица, район прибытия"
        self.element_is_visible(AddressFieldsLocators.TO_CITY).send_keys(self.to_city)
        self.element_to_be_clickable(AddressFieldsLocators.DROPDOWN_WINDOW_TO_CITY)
        self.element_is_visible(AddressFieldsLocators.TO_CITY).send_keys(Keys.ENTER)
        self.element_is_visible(AddressFieldsLocators.TO_ADDRESS).send_keys(self.to_address)

        # Нажатие на клавишу "Далее"
        self.element_is_visible(SubmitButtonLocator.SUBMIT_BUTTON).click()
