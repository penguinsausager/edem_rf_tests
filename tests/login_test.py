import time

from pages.login_page import LoginPage


class TestLogin:
    def test_login(self, driver):
        login_page = LoginPage(driver, 'https://едем.рф')
        login_page.open()
        login_page.fill_fields_and_submit()
        # Проверка, что авторизация прошла успешно
        assert driver.current_url == 'https://xn--d1abb2a.xn--p1ai/account/profile', 'URLS ARE NOT THE SAME'

