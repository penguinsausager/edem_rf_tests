import pytest

from config import auth, base_auth_url, base_url


@pytest.mark.run(order=4)
class TestLogin:

    def test_login(self, driver):
        auth(driver)
        assert driver.current_url == f'{base_auth_url()}/account/profile' or driver.current_url == \
               f'{base_url()}/account/profile', 'URLS ARE NOT THE SAME'
