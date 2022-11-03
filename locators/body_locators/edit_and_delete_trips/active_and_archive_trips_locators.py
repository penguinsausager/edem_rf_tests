from selenium.webdriver.common.by import By

"""Локаторы на странице "Активные поездки"."""


class ActiveAndArchiveTripsLocators:

    TRIP_DETAILS = (By.CSS_SELECTOR, '.button-md')
    ROUTES_ARCHIVE_BUTTON = (By.CSS_SELECTOR, '.js-account-routes-archive-handler')