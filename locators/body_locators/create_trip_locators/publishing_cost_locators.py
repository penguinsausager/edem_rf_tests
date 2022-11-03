from selenium.webdriver.common.by import By

"""Локаторы со страницы "Стоимость публикации объявления"."""


class PublishingCostLocators:
    # Чекбокс "Я соглашаюсь с условиями..."
    CHECKBOX = (By.CSS_SELECTOR, '.form-checkbox_caption')

    # Ссылка "Пользовательское соглашение"
    TERMS_OF_USE = (By.CSS_SELECTOR, 'color-link')