from django.db import models
from datetime import datetime
from website.models import Website

class Article(models.Model):
    subject = models.CharField(max_length=1024, blank=False)
    website = models.ForeignKey(Website, on_delete= models.DO_NOTHING)
    address = models.CharField(max_length=255, blank=False)
    upload_time = models.DateTimeField(default=datetime.now, blank=True)
    photo_url = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name = 'article content' 
        verbose_name_plural = 'article content' 

    def __str__(self):
        return self.subject[:10]


