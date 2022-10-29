import pathlib


def base_dir():
    path = pathlib.Path(__file__).parent.resolve()
    return path


def base_auth_url_beta():
    return 'https://beta.edemrf.com:452srCoS6F29JX6A3ttSk9nT23ZqtJy@beta.edemrf.com/'


def base_url_beta():
    return 'https://beta.edemrf.com'


def base_url_prod():
    return 'https://xn--d1abb2a.xn--p1ai'
