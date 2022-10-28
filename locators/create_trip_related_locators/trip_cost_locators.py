from selenium.webdriver.common.by import By

"""Локаторы с полем вводы стоимости поездки и чекбокса для цены больше рекомендуемого диапазона
на странице "Стоимость". При создании поездки."""


class TripCostLocators:

    COST_INPUT = (By.XPATH, '//input[@type="text"]')
    CLEAR_INPUT = (By.CSS_SELECTOR, 'form-group_icon-clear')

    HIGH_PRICE_CHECKBOX = (By.CSS_SELECTOR, '.form-checkbox_caption')
