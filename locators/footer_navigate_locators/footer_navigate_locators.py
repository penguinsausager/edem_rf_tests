from selenium.webdriver.common.by import By

"""Навигационные локаторы, доступные с любой страницы сайта"""


class FooterNavigateLocators:
    ABOUT = (By.XPATH, '(//a[@href="/about"])[2]')
    BLOG = (By.XPATH, '(//a[@href="/blog"])[2]')
    SAFETY = (By.XPATH, '(//a[@href="/safety"])[2]')

    PAYMENT_METHODS = (By.XPATH, '(//a[@href="/payments-methods"])[2]')
    FEEDBACK = (By.XPATH, '(//a[@href="/feedback/create"])[2]')
    FAQ = (By.XPATH, '(//a[@href="/faq"])[2]')

    BUS_STATIONS = (By.XPATH, '//a[@href="/buses/populars/regions"]')
    BUS_SCHEDULE = (By.XPATH, '//a[@href="/buses/routes"]')
    POPULAR_ROUTES = (By.XPATH, '(//a[@href="/routes/populars"])[2]')

    ADVERTISING = (By.XPATH, '(//a[@href="/advertising/create"])[2]')
    TERMS_OF_USE = (By.XPATH, '(//a[@href="/terms-of-use"])[2]')
    PRIVACY_POLICY = (By.XPATH, '(//a[@href="/privacy-policy"])[2]')

    APP_STORE = (By.XPATH, '//a[@class = "button-app"]')
    PLAY_MARKET = (By.XPATH, '//a[@class = "button-app"][2]')

    VK_LINK = (By.XPATH, '//a[@class="footer_social-link"][1]')
    OK_LINK = (By.XPATH, '//a[@class="footer_social-link"][2]')
    TELEGRAM_LINK = (By.XPATH, '//a[@class="footer_social-link"][3]')