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
    movie = MovieSerializer()

    class Meta:
        model = PopularReviewModel
        fields = ('id', 'movie', 'name', 'review', 'rating')


class RecentReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = RecentReviewModel
        fields = ('id', 'movie', 'name', 'review', 'rating')


class StatsSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = StatsModel
        fields = ('movie', 'views', 'likes', 'added_to_playlist')


class ImageSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = ImageModel
        fields = ('movie', 'release_year', 'poster_url', 'resized_poster')
