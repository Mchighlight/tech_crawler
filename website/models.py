from django.db import models

class SearchItem(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'search item' 
        verbose_name_plural = 'search item' 

    def __str__(self):
        return self.name


class Website(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False )
    description = models.TextField(blank=True)
    search_item = models.ManyToManyField(SearchItem)

    class Meta:
        verbose_name = 'website content' 
        verbose_name_plural = 'webstie content' 

    def __str__(self):
        return self.name



