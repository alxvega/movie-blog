from rest_framework import routers
from .views import MovieViewSet, PopularViewSet, RecentViewSet, StatsViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet, 'movies')
router.register('popular', PopularViewSet, 'popular')
router.register('recent', RecentViewSet, 'recent')
router.register('stats', StatsViewSet, 'stats')
router.register('images', ImageViewSet, 'images')

urlpatterns = router.urls
