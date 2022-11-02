from pages.base_page import BasePage
from locators.navigate_locators.submit_button_locators import SubmitButtonLocators
from locators.create_trip_related_locators.promo_locators import PromoLocators


class SelectPromoPage(BasePage):
    def select_free_promo(self):
        self.element_to_be_clickable(PromoLocators.FREE_PROMO).click()
        self.element_to_be_clickable(SubmitButtonLocators.SUBMIT_BUTTON).click()
