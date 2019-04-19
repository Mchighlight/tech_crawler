from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CrawlerViewSet, CronJobView

router = DefaultRouter()
router.register( 'crawler', CrawlerViewSet, basename='crawler' )
app_name = 'multitask'

urlpatterns = [
    path('', include(router.urls)),
    path('set/<int:id>/', CronJobView.as_view(), name='cronjob')
]

