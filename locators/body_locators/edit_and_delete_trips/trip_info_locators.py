from selenium.webdriver.common.by import By

"""Локаторы на странице с информацией о поездке <Город отправления> - <Город прибытия>"""


class TripInfoLocators:
    EDIT_BUTTON = (By.CSS_SELECTOR, '.form-button.button-lg')
