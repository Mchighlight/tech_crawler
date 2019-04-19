from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Website, SearchItem

from .serializers import WebsiteSerializer


WEBSITE_URL = reverse('api-website:one_end_point')


class PublicWebsiteApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(WEBSITE_URL)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

class PrivateWebsiteApiTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'password'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_Website(self):
        search_item = SearchItem.objects.create(name='chatbot')
        search_item.save()
        create_web = Website.objects.create(name='techcrunch')
        create_web.save()
        create_web.search_item.add(search_item)

        res = self.client.get(WEBSITE_URL)

        websites = Website.objects.all().order_by('-name')
        serializer = WebsiteSerializer(websites, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        #self.assertEqual(res.data, serializer.data)