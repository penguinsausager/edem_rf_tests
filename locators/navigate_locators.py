from selenium.webdriver.common.by import By


class NavigateLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.header_auth-box_sign :nth-child(2)')
    CREATE_TRIP_BUTTON = (By.CSS_SELECTOR, '.header_tour > .link-tour_create')
