from .models import MovieModel


def retrieve_movie_slugs():
    movies = MovieModel.objects.values('id', 'slug')
    return list(movies)
