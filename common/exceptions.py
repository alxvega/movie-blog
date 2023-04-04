class BadContentResponseError(Exception):
    pass


class PossibleBadContentResponseError(BadContentResponseError):
    pass


class FailContentResponseError(Exception):
    pass


class RequestError(Exception):
    pass
