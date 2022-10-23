from selenium.webdriver.common.by import By


class FillAddressFieldsLocators:

    CITY_FROM = (By.XPATH, '//input[@data-name="fromCityId"]')
    FROM_ADDRESS = (By.XPATH, '//input[@name="fromAddress"]')

    TO_CITY = (By.XPATH, '//input[@data-name="toCityId"]')
    TO_ADDRESS = (By.XPATH, '//input[@name="toAddress"]')

    DROPDOWN_WINDOW_CITY_FROM = (By.XPATH, '//div[@class="form-dropdown-title"]')
    DROPDOWN_WINDOW_TO_CITY = (By.CSS_SELECTOR, '.form-to .form-dropdown')