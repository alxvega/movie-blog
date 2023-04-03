import os
from dotenv import load_dotenv
from celery import shared_task
from celery.utils.log import get_task_logger
from sqlalchemy.orm import sessionmaker
from letterboxd.fetcher import (
    MoviesFetcher,
    PopularReviewsFetcher,
    RecentReviewsFetcher,
    ImageFetcher,
    StatsFetcher,
)

from letterboxd.parsing import ReviewsParser, MoviesParser, StatsParser, ImageParser

from letterboxd.persistance import retrieve_movie_slugs
from letterboxd.models import (
    get_engine,
    MovieModel,
    ImageModel,
    PopularReviewModel,
    RecentReviewModel,
    StatsModel,
)


logger = get_task_logger(__name__)
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))
engine = get_engine(
    user=os.getenv("DEFAULT_POSTGRES_USER"),
    password=os.getenv("DEFAULT_POSTGRES_PASSWORD"),
    host=os.getenv("DEFAULT_POSTGRES_SERVER"),
    port=os.getenv("DEFAULT_POSTGRES_PORT"),
    db=os.getenv("DEFAULT_POSTGRES_DB"),
)
Session = sessionmaker(bind=engine)


@shared_task()
def kickoff_initial_movies_data():
    fetcher = MoviesFetcher()
    pagination = fetcher.get_pagination()
    for page in range(1, pagination + 1):
        step = scrape_movie_page.s(page)
        step.link(save_movies.s())
        step.apply_async()


@shared_task(
    bind=True,
    # autoretry_for=(RequestError,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
)
def scrape_movie_page(self, page):
    fetcher = MoviesFetcher()
    response = fetcher.request(page)
    movies = MoviesParser().parse(response)
    return movies


@shared_task
def save_movies(movies):
    session = Session()
    for movie in movies:
        movie_record = MovieModel(**movie)
        session.add(movie_record)
    session.commit()
    session.close()


@shared_task
def kickoff_scrape_images():
    movies = retrieve_movie_slugs()
    for movie in movies:
        movie_slug = movie[0]
        step = scrape_movie_image.s(movie_slug, id=movie[1])
        step.link(save_images.s())
        step.apply_async()


@shared_task(
    bind=True,
    # autoretry_for=(RequestError, ),
    retry_backoff=True,
    retry_kwargs={"max_retries": 4},
)
def scrape_movie_image(self, movie_slug, **kwargs):
    response = ImageFetcher().request(movie_slug[0])
    images = ImageParser().parse(response)
    images.update(**kwargs)
    return images


@shared_task
def save_images(movie):
    session = Session()
    movie_record = ImageModel(**movie)
    session.add(movie_record)
    session.commit()
    session.close()


@shared_task
def kickoff_scrape_reviews(*args):
    process = args[0] if args else None
    movies = retrieve_movie_slugs()
    for movie in movies:
        movie_slug = movie[0]
        if not process or process == "popular":
            step = scrape_reviews.s(movie_slug, id=movie[1], process="popular")
            step.link(save_reviews.s("popular"))
            step.apply_async()
        if not process or process == "recent":
            step = scrape_reviews.s(movie_slug, id=movie[1], process="recent")
            step.link(save_reviews.s("recent"))
            step.apply_async()


@shared_task(
    bind=True,
    # autoretry_for=(RequestError,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 6},
)
def scrape_reviews(self, movie_slug, **kwargs):
    if kwargs["process"] == "popular":
        response = PopularReviewsFetcher().request(movie_slug)
        reviews = ReviewsParser().parse(response, id=kwargs["id"])
        return reviews
    elif kwargs["process"] == "recent":
        response = RecentReviewsFetcher().request(movie_slug)
        reviews = ReviewsParser().parse(response, id=kwargs["id"])
        return reviews


@shared_task
def save_reviews(reviews, process):
    session = Session()
    for review in reviews:
        if process == "popular":
            movie_record = PopularReviewModel(**review)
        elif process == "recent":
            movie_record = RecentReviewModel(**review)
        session.add(movie_record)
    session.commit()
    session.close()


@shared_task
def kickoff_scrape_stats():
    movies = retrieve_movie_slugs()
    for movie in movies:
        movie_slug = movie[0]
        step = scrape_movie_stats.s(movie_slug, id=movie[1])
        step.link(save_stats.s())
        step.apply_async()


@shared_task(
    bind=True,
    # autoretry_for=(RequestError,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 6},
)
def scrape_movie_stats(self, movie_slug, **kwargs):
    response = StatsFetcher().request(movie_slug[0])
    stats = StatsParser().parse(response)
    stats.update(**kwargs)
    return stats


@shared_task
def save_stats(stats):
    session = Session()
    movie_record = StatsModel(**stats)
    session.add(movie_record)
    session.commit()
    session.close()
