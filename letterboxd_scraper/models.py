from django.db import models
from django.utils import timezone


class MovieModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    extraction_datetime = models.DateTimeField(default=timezone.now)


class ImageModel(models.Model):
    movie = models.OneToOneField(MovieModel, on_delete=models.CASCADE, primary_key=True)
    release_year = models.IntegerField(null=True, blank=True)
    poster_url = models.URLField(null=True, blank=True)
    resized_poster = models.URLField(null=True, blank=True)
    extraction_datetime = models.DateTimeField(default=timezone.now)


class PopularReviewModel(models.Model):
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    extraction_datetime = models.DateTimeField(default=timezone.now)


class RecentReviewModel(models.Model):
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    extraction_datetime = models.DateTimeField(default=timezone.now)


class StatsModel(models.Model):
    movie = models.OneToOneField(MovieModel, on_delete=models.CASCADE, primary_key=True)
    views = models.IntegerField()
    likes = models.IntegerField()
    added_to_playlist = models.IntegerField()
    extraction_datetime = models.DateTimeField(default=timezone.now)
