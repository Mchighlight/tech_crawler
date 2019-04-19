from django.urls import path
from .views import WebsiteAPIDetailView, WebsiteOneAPIView

urlpatterns = [
    path('<int:id>/', WebsiteAPIDetailView.as_view(), name='detail'),
    path('', WebsiteOneAPIView.as_view(), name='one_end_point')
]

