from rest_framework import permissions, viewsets, status, generics, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .task import cronjob
from .models import Cronjob
from .serializers import CronJobSerializer


class CrawlerViewSet( viewsets.ViewSet):
    @list_route(methods=['post'], permission_classes=[], authentication_classes=[],url_path='start_crawler')
    def task(self, request):
        data = request.data
        try:
            cronjob(data)
            return Response(data={"message": "asynchronous updating..."}, status=status.HTTP_200_OK) 
        except:
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)  

class CronJobView(generics.RetrieveAPIView,
                  mixins.UpdateModelMixin
):

    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CronJobSerializer
    queryset = Cronjob.objects.all()
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

