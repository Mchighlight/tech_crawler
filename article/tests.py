from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Article
from website.models import Website, SearchItem

from .serializers import ArticleSerializer


ARTICLE_URL = reverse('api-article:one_end_point')


class PublicArticleApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(ARTICLE_URL)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

class PrivateAritcleApiTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'password'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_Article(self):
        create_web = Website.objects.create(name='techcrunch')
        search_item = SearchItem.objects.create(name='cybersecurity')
        Article.objects.create(website=create_web, subject="123", address="www.google.com", topic=search_item)

        res = self.client.get(ARTICLE_URL)

        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        #self.assertEqual(res.data, serializer.data)
