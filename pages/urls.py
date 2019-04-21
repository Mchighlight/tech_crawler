from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('ai', views.ai, name='ai'),
    path('iot', views.iot, name='iot'),
    path('cloud_computing', views.cloud_computing, name='cloud_computing'),
    path('about', views.about, name='about'),
]
