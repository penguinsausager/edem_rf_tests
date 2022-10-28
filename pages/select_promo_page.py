from pages.base_page import BasePage
from locators.submit_button_locator import SubmitButtonLocator
from locators.create_trip_related_locators.promo_locators import PromoLocators


class SelectPromoPage(BasePage):
    def select_promo(self):
        self.element_to_be_clickable(PromoLocators.FIRST_PROMO).click()
        self.element_to_be_clickable(SubmitButtonLocator.SUBMIT_BUTTON).click()
