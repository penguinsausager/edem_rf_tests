import os
import pathlib

__prod_url = os.getenv('BASE_URL_PROD')
__beta_url = os.getenv('BASE_URL_BETA')
__beta_login = os.getenv('AUTH_LOGIN_BETA')
__beta_password = os.getenv('AUTH_LOGIN_PASSWORD')


def base_dir():
    path = pathlib.Path(__file__).parent.resolve()
    return path


def cookies_directory_path():
    return f'{base_dir()}/cookies'


def base_auth_url():
    if os.getenv('MODE') == 'BETA':
        return f'{__beta_url}:{__beta_password}@{__beta_login}'
    elif os.getenv('MODE') == 'PROD':
        return __prod_url


def base_url():
    if os.getenv('MODE') == 'BETA':
        return __beta_url
    elif os.getenv('MODE') == 'PROD':
        return __prod_url


def auth(driver):
    from pages.main_page import MainPage
    from pages.login_page import LoginPage

    main_page = MainPage(driver)
    login_page = LoginPage(driver, base_auth_url())
    login_page.open()
    main_page.login_click()

    __phone_number = get_phone_number()

    if not os.path.exists(cookies_directory_path()):
        os.mkdir(cookies_directory_path())

    if os.path.exists(f'{cookies_directory_path()}/{__phone_number}_cookies'):
        login_page.set_cookie()
    else:
        login_page.fill_fields_and_submit()
        login_page.save_cookie()


def get_phone_number():
    if os.getenv('MODE') == 'BETA':
        return os.getenv('PHONE_NUMBER_BETA')
    elif os.getenv('MODE') == 'PROD':
        return os.getenv('PHONE_NUMBER_PROD')
