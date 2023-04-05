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
        fields = ('title', 'slug', 'rating')


class PopularReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularReviewModel
        fields = ('review_id', 'name', 'review', 'rating')


class RecentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentReviewModel
        fields = ('review_id', 'name', 'review', 'rating')


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatsModel
        fields = ('views', 'likes', 'added_to_playlist')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('release_year', 'poster_url', 'resized_poster')
