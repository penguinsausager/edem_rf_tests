import time

from config import auth, base_auth_url, base_url


class TestLogin:

    def test_login(self, driver):
        auth(driver)
        assert driver.current_url == f'{base_auth_url()}/account/profile', 'URLS ARE NOT THE SAME'