from selenium.webdriver.common.by import By
from config import auth, base_auth_url, base_url


class TestLogin:

    def test_login(self, driver):
        auth(driver)
        assert driver.current_url == f'{base_auth_url()}/account/profile' or driver.current_url == \
               f'{base_url()}/account/profile', 'URLS ARE NOT THE SAME'
        # todo: перенести в тест верстки(?)
        assert driver.find_element(By.CSS_SELECTOR, '.profile-user'), 'LOCATOR NOT FOUND'
        assert driver.find_element(By.XPATH, '//a[@href="/account/profile/info"]'), 'LOCATOR NOT FOUND'
        assert driver.find_element(By.XPATH, '//a[@href="/account/profile/notifications"]'), 'LOCATOR NOT FOUND'
        assert driver.find_element(By.XPATH, '(//a[@href="/account/reviews"])[2]'), 'LOCATOR NOT FOUND'
        assert driver.find_element(By.XPATH, '(//a[@href="/account/balance"])[2]'), 'LOCATOR NOT FOUND'
        assert driver.find_element(By.XPATH, '//a[@href="/account/balance/transfers"]'), 'LOCATOR NOT FOUND'
        assert driver.find_element(By.XPATH, '//a[@href="/account/refunds/cards"]'), 'LOCATOR NOT FOUND'
        assert driver.find_element(By.CSS_SELECTOR, '.profile_button-logout'), 'LOCATOR NOT FOUND'
