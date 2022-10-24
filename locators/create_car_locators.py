from selenium.webdriver.common.by import By


class CreateCarLocators:
    CAR_BRAND_INPUT = (By.XPATH, '//input[@data-name="brandId"]')
    CAR_MODEL_INPUT = (By.XPATH, '//input[@data-name="modelId"]')
    CAR_YEAR = (By.XPATH, '//input[@name="year"]')
    PLATE_NUMBER = (By.XPATH, '//input[@name="plateNumber"]')
    CAR_COLOR = (By.XPATH, '//span[@style="background: #FFC0CB;"]')