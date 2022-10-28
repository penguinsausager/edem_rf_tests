import pickle
import time

from selenium.webdriver.common.alert import Alert

from auth_data import phone_number
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from base import base_dir


class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def fill_alert_fields(self):
        pass

    def save_cookie(self):
        print(base_dir())
        pickle.dump(self.driver.get_cookies(), open(f"{base_dir()}/cookies/{phone_number}_cookies", "wb"))
        # self.driver.delete_all_cookies()

    def set_cookie(self):
        for cookie in pickle.load(open(f"{base_dir()}/cookies/{phone_number}_cookies", "rb")):
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_to_be_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
