from rest_framework import serializers
from .models import Cronjob

class CronJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cronjob
        fields = '__all__'


