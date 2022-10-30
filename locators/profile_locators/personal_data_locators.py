from selenium.webdriver.common.by import By


class PersonalDataLocators:

    USERNAME = (By.CSS_SELECTOR, '.js-account-update-personal-name-handler')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, '.js-account-update-personal-birthday-handler')
    SEX = (By.CSS_SELECTOR, '.js-account-update-personal-sex-handler')
    EMAIL = (By.CSS_SELECTOR, '.js-account-update-email-handler')
    PHONE_NUMBER = (By.CSS_SELECTOR, '.js-account-update-phone-handler')
    PASSWORD = (By.CSS_SELECTOR, '.js-account-update-password-handler')
    AUTO = (By.CSS_SELECTOR, '[href="/account/cars"]')
    DELETE_ACCOUNT = (By.CSS_SELECTOR, '.js-account-remove-handler')
