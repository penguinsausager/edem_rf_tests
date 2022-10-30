from selenium.webdriver.common.by import By

"""Навигационные локаторы, доступные с любой страницы сайта"""


class HeaderNavigateLocators:

    EDEMRF_LOGO = (By.CSS_SELECTOR, '.header_logo-type')

    TRIP_SEARCH = (By.CSS_SELECTOR, '.header_tour .link-tour_search')
    CREATE_TRIP_BUTTON = (By.CSS_SELECTOR, '.header_tour > .link-tour_create')

    MESSAGES = (By.XPATH, '//div[@class="notice-display js-notice-display "]')
    NOTICE = (By.XPATH, '//div[@class="notice-display js-notice-display"]')

    DROPDOWN_MENU = (By.CSS_SELECTOR, '.sm.no-link')

    BALANCE = (By.XPATH, '(//div[@class="header_menu_name-relative"])[1]')
    DRIVER = (By.XPATH, '(//div[@class="header_menu_name-relative"])[2]')
    PASSENGER = (By.XPATH, '(//div[@class="header_menu_name-relative"])[3]')
    REVIEWS = (By.XPATH, '(//div[@class="header_menu_name-relative"])[4]')
    MY_PROFILE = (By.XPATH, '(//div[@class="header_menu_name-relative"])[5]')
    LOGOUT = (By.CSS_SELECTOR, '.header_menu-nav_link.js-auth-logout')

    REGISTER_BUTTON = (By.XPATH, '(//a[@class="header_auth-link"])[1]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.header_auth-box_sign :nth-child(2)')



    # ===перенести в другие локаторы
    PROFILE_OPTION = (By.XPATH, '//a[@class="profile_option"]')
