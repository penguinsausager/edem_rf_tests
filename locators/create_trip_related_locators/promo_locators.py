from selenium.webdriver.common.by import By

"""Локаторы на странице "Продвиньте ваше объявление"."""


class PromoLocators:

    FIRST_PROMO = (By.XPATH, '(//div[@class="route-promo_name-wrapper"])[1]')
    SECOND_PROMO = (By.XPATH, '(//div[@class="route-promo_name-wrapper"])[2]')
    THIRD_PROMO = (By.XPATH, '(//div[@class="route-promo_name-wrapper"])[3]')
    FOURTH_PROMO = (By.XPATH, '(//div[@class="route-promo_name-wrapper"])[4]')
