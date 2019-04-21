from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Article
from website.serializers import WebsiteSerializer
from website.models import Website


class ArticleSerializer(serializers.ModelSerializer):
    web_uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Article
        fields = [
            'id',
            'web_uri',
            'website',
            'subject',
            'address',
            'upload_time',
            'topic'
        ]
        read_only_Fields = ('id',)

    def validate(self, data):
        subject = data.get("subject", None)
        if subject == "":
            subject = None
        address = data.get("address", None)
        if subject is None and address is None :
            raise serializers.ValidationError("subject or address item is required")
        return data


    def get_web_uri(self,obj):
        request = self.context.get('request')
        return reverse("api-website:detail", kwargs={'id':obj.website.id}, request=request)

    