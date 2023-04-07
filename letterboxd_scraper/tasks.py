from celery import shared_task
from celery.utils.log import get_task_logger
from .persistance import retrieve_movie_slugs
from .scraping.parser import ReviewsParser, MoviesParser, StatsParser, ImageParser
from .scraping.fetcher import (
    MoviesFetcher,
    PopularReviewsFetcher,
    RecentReviewsFetcher,
    ImageFetcher,
    StatsFetcher,
)
from .models import (
    MovieModel,
    ImageModel,
    PopularReviewModel,
    RecentReviewModel,
    StatsModel,
)
from common.exceptions import (
    RequestError,
    StaleProxyError,
)


logger = get_task_logger(__name__)

WORKERS = 7
WORKERS_RATE_LIMIT = 3


# Triggers
@shared_task()
def kickoff_initial_movies_data():
    fetcher = MoviesFetcher()
    pagination = fetcher.get_pagination()
    for page in range(1, pagination + 1):
        step = scrape_movie_page.s(page)
        step.link(save_movies.s())
        step.apply_async()


@shared_task
def kickoff_scrape_stats():
    movies = retrieve_movie_slugs()
    for movie in movies:
        step = scrape_movie_stats.s(movie_slug=movie[1], id=movie[0])
        step.link(save_stats.s())
        step.apply_async()


@shared_task
def kickoff_scrape_images():
    movies = retrieve_movie_slugs()
    for movie in movies:
        step = scrape_movie_image.s(movie_slug=movie[1], id=movie[0])
        step.link(save_images.s())
        step.apply_async()


@shared_task
def kickoff_scrape_reviews(*args):
    process = args[0] if args else None
    movies = retrieve_movie_slugs()
    for movie in movies:
        if not process or process == "popular":
            step = scrape_reviews.s(movie_slug=movie[1], process="popular", movie_id=movie[0])
            step.link(save_reviews.s("popular"))
            step.apply_async()
        if not process or process == "recent":
            step = scrape_reviews.s(movie_slug=movie[1], process="recent", movie_id=movie[0])
            step.link(save_reviews.s("recent"))
            step.apply_async()


# Scrapes
@shared_task(
    bind=True,
    default_retry_delay=600,
    autoretry_for=(RequestError, StaleProxyError),
    retry_kwargs={"max_retries": 5},
)
def scrape_movie_page(self, page):
    fetcher = MoviesFetcher()
    response = fetcher.request(page)
    movies = MoviesParser().parse(response)
    print(f'Scraped {page}')
    return movies


@shared_task(
    bind=True,
    default_retry_delay=600,
    autoretry_for=(RequestError, StaleProxyError),
    retry_kwargs={"max_retries": 5},
    rate_limit=f'{1200 // WORKERS}/m',
    # rate_limit=f'500/m',
)
def scrape_movie_image(self, movie_slug, **kwargs):
    response = ImageFetcher().request(movie_slug)
    images = ImageParser().parse(response, **kwargs)
    return images


@shared_task(
    bind=True,
    default_retry_delay=600,
    autoretry_for=(RequestError, StaleProxyError),
    retry_kwargs={"max_retries": 5},
    rate_limit=f'{1200 // WORKERS}/m',
)
def scrape_reviews(self, movie_slug, process, **kwargs):
    if process == "popular":
        response = PopularReviewsFetcher().request(movie_slug)
        reviews = ReviewsParser().parse(response, **kwargs)
        return reviews
    elif process == "recent":
        response = RecentReviewsFetcher().request(movie_slug)
        reviews = ReviewsParser().parse(response, **kwargs)
        return reviews


@shared_task(
    bind=True,
    default_retry_delay=600,
    autoretry_for=(RequestError, StaleProxyError),
    retry_kwargs={"max_retries": 5},
    rate_limit=f'{1200 // WORKERS}/m',
)
def scrape_movie_stats(self, movie_slug, **kwargs):
    response = StatsFetcher().request(movie_slug)
    stats = StatsParser().parse(response, **kwargs)
    return stats


# Saves
@shared_task
def save_movies(movies):
    MovieModel.objects.bulk_create([MovieModel(**movie) for movie in movies], ignore_conflicts=True)


@shared_task
def save_reviews(reviews, process):
    if process == 'popular':
        PopularReviewModel.objects.bulk_create([PopularReviewModel(**review) for review in reviews])
    elif process == 'recent':
        RecentReviewModel.objects.bulk_create([RecentReviewModel(**review) for review in reviews])


@shared_task
def save_stats(stats):
    StatsModel.objects.create(**stats)


@shared_task
def save_images(movie):
    ImageModel.objects.create(**movie)
