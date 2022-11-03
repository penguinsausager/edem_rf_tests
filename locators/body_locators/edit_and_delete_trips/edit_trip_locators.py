from selenium.webdriver.common.by import By

"""Локаторы на странице "Редактирование" маршрута."""


class EditTripLocators:
    DELETE_TRIP = (By.CSS_SELECTOR, '.js-account-routes-remove-handler')
