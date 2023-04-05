import requests
import urllib3
from selectolax.parser import HTMLParser
from common.utils import (
    generate_user_agents,
    get_random_user_agent,
    get_proxy_session,
)

urllib3.disable_warnings()

USER_AGENTS = generate_user_agents((107, 109))


class LetterboxdFetcher:
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Host": "letterboxd.com",
        "Referer": "https://www.google.com/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "{}",
    }

    def __init__(self) -> None:
        # self.headers[
        #     "User-Agent"
        # ] = 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
        # self.proxy = None
        self.headers["User-Agent"] = get_random_user_agent(USER_AGENTS)
        self.proxy = get_proxy_session()

    def request(self, format_value, **kwargs):
        return requests.get(
            self.url.format(format_value),
            headers=self.headers,
            proxies=self.proxy,
            verify=False,
        )


class PopularReviewsFetcher(LetterboxdFetcher):
    url = "https://letterboxd.com/ajax/{}/popular-reviews/"


class RecentReviewsFetcher(LetterboxdFetcher):
    url = "https://letterboxd.com/ajax/{}/recent-reviews/"


class ImageFetcher(LetterboxdFetcher):
    url = "https://letterboxd.com/ajax/poster/film/{}/std/110x165/list-item/"


class StatsFetcher(LetterboxdFetcher):
    url = "https://letterboxd.com/esi/film/{}/stats/"


class MoviesFetcher(LetterboxdFetcher):
    url = "https://letterboxd.com/films/ajax/popular/this/week/page/{}/?esiAllowFilters=true"

    def get_pagination(self):
        response = requests.get(self.url.format(1), headers=self.headers)
        tree = HTMLParser(response.content)
        total_movies = tree.css_first("p[class=ui-block-heading]").text().strip()
        total_movies = int("".join(filter(lambda x: str.isdigit(x), total_movies)))
        movies_per_page = len([node for node in tree.css('li[class="listitem poster-container"]')])
        pagination = total_movies / movies_per_page
        pagination = pagination if pagination % 1 == 0 else int(pagination + 1)
        return int(pagination)
