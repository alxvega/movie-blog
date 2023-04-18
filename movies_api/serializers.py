from rest_framework import serializers
from letterboxd_scraper.models import (
    MovieModel,
    PopularReviewModel,
    RecentReviewModel,
    StatsModel,
    ImageModel,
)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = ('id', 'title', 'slug', 'rating')


class PopularReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularReviewModel
        fields = ('id', 'name', 'review', 'rating', 'movie_id')


class RecentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentReviewModel
        fields = ('id', 'name', 'review', 'rating', 'movie_id')


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatsModel
        fields = ('views', 'likes', 'added_to_playlist', 'movie_id')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('release_year', 'poster_url', 'resized_poster', 'movie_id')
