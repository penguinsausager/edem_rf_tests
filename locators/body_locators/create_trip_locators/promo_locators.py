from selenium.webdriver.common.by import By

"""Локаторы на странице "Продвиньте ваше объявление"."""


class PromoLocators:

    FREE_PROMO = (By.XPATH, '(//div[@class="route-promo_name-wrapper"])[1]')
    STANDARD_PROMO = (By.XPATH, '(//div[@class="route-promo_name-wrapper"])[2]')
    STANDARD_PLUS_PROMO = (By.XPATH, '(//div[@class="route-promo_name-wrapper"])[3]')
    PREMIUM_PROMO = (By.XPATH, '(//div[@class="route-promo_name-wrapper"])[4]')
