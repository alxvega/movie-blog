# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import pagination
from letterboxd_scraper.models import (
    MovieModel,
    PopularReviewModel,
    RecentReviewModel,
    StatsModel,
    ImageModel,
)
from .serializers import (
    MovieSerializer,
    PopularReviewSerializer,
    RecentReviewSerializer,
    StatsSerializer,
    ImageSerializer,
)


class MoviePagination(pagination.PageNumberPagination):
    page_size = 20


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    permission_classes = [permissions.AllowAny]


class PopularViewSet(viewsets.ModelViewSet):
    queryset = PopularReviewModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PopularReviewSerializer


class RecentViewSet(viewsets.ModelViewSet):
    queryset = RecentReviewModel.objects.all()
    serializer_class = RecentReviewSerializer
    permission_classes = [permissions.AllowAny]


class StatsViewSet(viewsets.ModelViewSet):
    queryset = StatsModel.objects.all()
    serializer_class = StatsSerializer
    permission_classes = [permissions.AllowAny]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]
