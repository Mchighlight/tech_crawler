from rest_framework import serializers
from .models import Website, SearchItem

class SearchItemSerialzier(serializers.ModelSerializer):
    class Meta:
        model = SearchItem
        fields = [
            'id',
            'name'
        ]
        read_only_Fields = ('id',)

class WebsiteSerializer(serializers.ModelSerializer):
    search_item = SearchItemSerialzier(many=True, read_only=True )
    class Meta :
        model = Website
        fields = [
            'id',
            'name',
            'description',
            'search_item'
        ]
        read_only_Fields = ('id',)

    def validate(self, data):
        name = data.get("name", None)
        if name == "":
            name = None
        search_item = data.get("search_item", None)
        if name is None and search_item is None :
            raise serializers.ValidationError("Name or search item is required")
        return data



