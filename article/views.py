from rest_framework import mixins, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer


class ArticleAPIDetailView(
            mixins.UpdateModelMixin,
            generics.RetrieveAPIView
):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class ArticleOneAPIView(
            mixins.CreateModelMixin,
            generics.ListAPIView
):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer
    search_fields = ('subject', 'website')
    queryset = Article.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


