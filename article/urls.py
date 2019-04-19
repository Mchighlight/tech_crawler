from django.urls import path
from .views import ArticleAPIDetailView, ArticleOneAPIView

urlpatterns = [
    path('<int:id>/', ArticleAPIDetailView.as_view(), name='detail'),
    path('', ArticleOneAPIView.as_view(), name='one_end_point')
]

