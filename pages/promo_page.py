from pages.base_page import BasePage
from locators.submit_button_locator import SubmitButtonLocator
from locators.body_locators.create_trip_locators.promo_locators import PromoLocators


class PromoPage(BasePage):
    def select_free_promo(self):
        self.element_to_be_clickable(PromoLocators.FREE_PROMO).click()
        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()
