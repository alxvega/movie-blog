import re
from selectolax.parser import HTMLParser


def extract_text(selector):
    try:
        return selector.text()
    except AttributeError:
        return None


def normalize(text):
    try:
        return re.sub(r"\s+", " ", text).strip()
    except AttributeError:
        return None


def extract_number(string):
    if not string:
        return None
    return int("".join(filter(lambda x: str.isdigit(x), string)))


class ReviewsParser:
    def parse(self, response, **kwargs):
        tree = HTMLParser(response.content)
        movie_grid = tree.css('li[class*="film-detail"]')
        items = []
        for review in movie_grid:
            author = review.css_first('strong[class="name"]')
            text = review.css_first('div[class*="body-text"]')
            rating = review.css_first('span[class*="rating"]')
            review_item = {
                "name": normalize(extract_text(author)),
                "review": normalize(extract_text(text)),
                "rating_stars": normalize(extract_text(rating)),
            }
            review_item.update(kwargs)
            items.append(review_item)
        return items


class MoviesParser:
    def parse(self, response):
        tree = HTMLParser(response.content)
        movie_grid = tree.css('li[class*="listitem poster-container"]')
        movies = []
        for node in movie_grid:
            movie_info = node.css_first("div").attributes
            movie_rating = node.attrs.get("data-average-rating", None)
            movie_slug = movie_info["data-film-slug"].split("/")[-2]
            movie_id = movie_info["data-film-id"]
            movie_title = normalize(node.css_first("img").attrs["alt"])
            if not movie_title:
                movie_title = movie_slug.replace("-", " ").title()
            info = {
                "id": movie_id,
                "title": normalize(movie_title),
                "slug": movie_slug,
                "rating": movie_rating,
            }
            movies.append(info)
        return movies


class StatsParser:
    def parse(self, response, **kwargs):
        tree = HTMLParser(response.content)
        views = extract_text(tree.css_first('li[class*="stat filmstat-watches"]'))
        playlists_number = extract_text(tree.css_first('li[class*="stat filmstat-lists"]'))
        likes = extract_text(tree.css_first('li[class*="stat filmstat-likes"]'))
        item = {
            "views": extract_number(views),
            "likes": extract_number(likes),
            "added_to_playlist": extract_number(playlists_number),
        }
        item.update(kwargs)
        return item


class ImageParser:
    def parse(self, response, **kwargs):
        tree = HTMLParser(response.content)
        image = tree.css_first("img").attrs.get("srcset", None)
        resized_image = tree.css_first("img").attrs["src"]
        movie_release_year = tree.css_first('li[class*="film-poster"]').attrs[
            "data-film-release-year"
        ]
        item = {
            "release_year": int(movie_release_year) if movie_release_year else None,
            "poster_url": image,
            "resized_poster": resized_image,
        }
        item.update(kwargs)
        return item
