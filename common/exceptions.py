from requests.exceptions import ConnectionError


class StaleProxyError(Exception):
    pass


class BadContentResponseError(Exception):
    pass


class PossibleBadContentResponseError(BadContentResponseError):
    pass


class FailContentResponseError(Exception):
    pass


class RequestError(Exception):
    pass


def catch_proxy_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionError:
            raise StaleProxyError

    return wrapper
