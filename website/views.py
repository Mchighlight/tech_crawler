from rest_framework import mixins, generics, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Website, SearchItem
from .serializers import WebsiteSerializer


class WebsiteAPIDetailView(
            mixins.UpdateModelMixin,
            generics.RetrieveAPIView
):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = WebsiteSerializer
    queryset = Website.objects.all()
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class WebsiteOneAPIView(
            mixins.CreateModelMixin,
            generics.ListAPIView
):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = WebsiteSerializer
    search_fields = ('description', 'name')
    queryset = Website.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


