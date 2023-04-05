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


class CommonPaginator(pagination.PageNumberPagination):
    page_size = 100


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
    pagination_class = CommonPaginator
    permission_classes = [permissions.AllowAny]


class PopularViewSet(viewsets.ModelViewSet):
    queryset = PopularReviewModel.objects.all()
    permission_classes = [permissions.AllowAny]
    pagination_class = CommonPaginator
    serializer_class = PopularReviewSerializer


class RecentViewSet(viewsets.ModelViewSet):
    queryset = RecentReviewModel.objects.all()
    serializer_class = RecentReviewSerializer
    pagination_class = CommonPaginator
    permission_classes = [permissions.AllowAny]


class StatsViewSet(viewsets.ModelViewSet):
    queryset = StatsModel.objects.all()
    serializer_class = StatsSerializer
    pagination_class = CommonPaginator
    permission_classes = [permissions.AllowAny]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    pagination_class = CommonPaginator
    permission_classes = [permissions.AllowAny]
