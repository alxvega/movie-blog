from .models import MovieModel


def retrieve_movie_slugs():
    movies = MovieModel.objects.values('slug', 'id').values_list()
    return movies
