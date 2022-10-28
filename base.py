import pathlib


def base_dir():
    path = pathlib.Path(__file__).parent.resolve()
    return path


def base_url_beta():
    return 'https://beta.edemrf.com/'


def base_url_prod():
    return 'https://едем.рф'