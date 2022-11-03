from selenium.webdriver.common.by import By

"""Локаторы установки даты и времени на странице "Когда и во сколько планируете выезд"?"""


class DateAndTimeLocators:

    INPUT_DATE_FIELD = (By.XPATH, '//input[@data-name="createdDate"]')
    SELECT_NEXT_MONTH_BUTTON = (By.XPATH, '//div[@data-action="next"]')
    DAY_OF_THE_CURRENT_MONTH = (By.XPATH, '(//div[@data-date="1"])[1]')

    INPUT_TIME_FIELD = (By.XPATH, '//input[@name="createdTime"]')
    HOUR_SELECT = (By.CSS_SELECTOR, '.clockpicker-dial :nth-child(17)')
    MINUTE_SELECT = (By.CSS_SELECTOR, '.clockpicker-minutes > div:nth-child(4)')

    RETURN_TRIP = (By.CSS_SELECTOR, '.form-button.button-md.button-gray.js-routes-drafts-add-reverse-route-handler')
