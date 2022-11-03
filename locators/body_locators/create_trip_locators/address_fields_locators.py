from selenium.webdriver.common.by import By

"""Локаторы на странице "Создание поездки"."""


class AddressFieldsLocators:

    CITY_FROM = (By.XPATH, '//input[@data-name="fromCityId"]')
    FROM_ADDRESS = (By.XPATH, '//input[@name="fromAddress"]')

    TO_CITY = (By.XPATH, '//input[@data-name="toCityId"]')
    TO_ADDRESS = (By.XPATH, '//input[@name="toAddress"]')

    DROPDOWN_WINDOW_CITY_FROM = (By.XPATH, '//div[@class="form-dropdown-title"]')
    DROPDOWN_WINDOW_TO_CITY = (By.CSS_SELECTOR, '.form-to .form-dropdown')

    ADD_WAYPOINT_BUTTON = (By.CSS_SELECTOR, '.button-name')

    # Изменить цифру в конце, если требуется добавить несколько промежуточных пунктов
    WAYPOINT_CITY_FROM = (By.XPATH, '//input[@data-name="throughCitiesIds0"]')
    WAYPOINT_TO_CITY = (By.XPATH, '//input[@data-name="throughAddress0"]')
    DELETE_WAYPOINT_BUTTON = (By.XPATH, '//div[@class="remove-handle js-routes-drafts-remove-through-city-handler"]')
