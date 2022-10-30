from selenium.webdriver.common.by import By

"""Локаторы для редактирования/создания автомобиля на странице "Создание автомобиля"."""


class CarLocators:

    CAR_BRAND_INPUT = (By.XPATH, '//input[@data-name="brandId"]')
    CAR_MODEL_INPUT = (By.XPATH, '//input[@data-name="modelId"]')

    CAR_YEAR = (By.XPATH, '//input[@name="year"]')
    PLATE_NUMBER = (By.XPATH, '//input[@name="plateNumber"]')

    CAR_COLOR = (By.XPATH, '//span[@style="background: #FFC0CB;"]')

    SELECT_CAR_FIRST = (By.XPATH, '(//div[@class="route-car_wrap"])[1]')
    SELECT_CAR_SECOND = (By.XPATH, '(//div[@class="route-car_wrap"])[2]')
    SELECT_CAR_THIRD = (By.XPATH, '(//div[@class="route-car_wrap"])[3]')

    # Кнопка "Удалить"
    DELETE_CAR = (By.CSS_SELECTOR, '.js-account-cars-remove-handler')

    # Кнопка "Удалить" на всплывающем окне "Подтверждение удаления"
    DELETE_CONFIRM = (By.CSS_SELECTOR, '.js-popup-confirm')