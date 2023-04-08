from django.db import models


class MovieModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    rating = models.FloatField(null=True)
    extraction_datetime = models.DateTimeField(null=True, auto_now_add=True)


class PopularReviewModel(models.Model):
    movie_id = models.CharField(null=True)
    name = models.CharField(max_length=800)
    review = models.TextField(max_length=800)
    rating = models.CharField(max_length=800, null=True)
    extraction_datetime = models.DateTimeField(null=True, auto_now_add=True)


class RecentReviewModel(models.Model):
    movie_id = models.CharField(null=True)
    name = models.CharField(max_length=800)
    review = models.TextField(max_length=800)
    rating = models.CharField(max_length=800, null=True)
    extraction_datetime = models.DateTimeField(null=True, auto_now_add=True)


class StatsModel(models.Model):
    views = models.IntegerField()
    likes = models.IntegerField()
    added_to_playlist = models.IntegerField()
    extraction_datetime = models.DateTimeField(null=True, auto_now_add=True)


class ImageModel(models.Model):
    release_year = models.IntegerField(null=True)
    poster_url = models.CharField(max_length=800, null=True)
    resized_poster = models.CharField(max_length=800)
    extraction_datetime = models.DateTimeField(null=True, auto_now_add=True)
