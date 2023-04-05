from .models import MovieModel


def retrieve_movie_slugs():
    movies = MovieModel.objects.values_list('id', 'slug')
    return list(movies)
