from selenium.webdriver.common.by import By


class ProfileLocators:

    PROFILE_USER_INFO = (By.CSS_SELECTOR, '.profile-user')

    PERSONAL_DATA = (By.XPATH, '//a[@href="/account/profile/info"]')
    NOTIFICATIONS = (By.XPATH, '//a[@href="/account/profile/notifications"]')
    REVIEWS = (By.XPATH, '(//a[@href="/account/reviews"])[2]')

    BALANCE = (By.XPATH, '(//a[@href="/account/balance"])[2]')
    BALANCE_TRANSFERS = (By.XPATH, 'href="/account/balance/transfers"')
    REFUND_CARS = (By.XPATH, '//a[@href="/account/refunds/cards"]')

    LOGOUT = (By.CSS_SELECTOR, '.profile_button-logout')



