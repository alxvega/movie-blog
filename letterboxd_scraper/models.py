from django.db import models


class MovieModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    rating = models.FloatField(null=True)


class PopularReviewModel(models.Model):
    # movie_id = models.ForeignKey(MovieModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.CharField(max_length=255)


class RecentReviewModel(models.Model):
    name = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.CharField(max_length=255)


class StatsModel(models.Model):
    views = models.IntegerField()
    likes = models.IntegerField()
    added_to_playlist = models.IntegerField()


class ImageModel(models.Model):
    release_year = models.IntegerField(null=True)
    poster_url = models.CharField(max_length=255, null=True)
    resized_poster = models.CharField(max_length=255)
