import pickle
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from config import base_dir, get_phone_number, cookies_directory_path


class BasePage:
    __timeout__ = 5
    __phone_number__ = get_phone_number()

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        load_dotenv()

    def open(self):
        self.driver.get(self.url)

    def save_cookie(self):
        print(base_dir())
        pickle.dump(self.driver.get_cookies(),
                    open(f"{cookies_directory_path()}/{self.__phone_number__}_cookies", "wb"))

    def set_cookie(self):
        for cookie in pickle.load(open(f"{cookies_directory_path()}/{self.__phone_number__}_cookies", "rb")):
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def element_is_visible(self, locator, timeout=__timeout__):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=__timeout__):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_to_be_clickable(self, locator, timeout=__timeout__):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
