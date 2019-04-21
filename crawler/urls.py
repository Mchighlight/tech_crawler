from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API')
urlpatterns = [
    path('docs/', schema_view),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('api/website/', include(('website.urls', "api-website"))),
    path('api/article/', include(('article.urls', "api-article"))),
    path('api/multitask/', include(('multitask.urls', "api-multitask"))),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
