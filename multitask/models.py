from django.db import models

class Cronjob(models.Model):
    trigger_time = models.IntegerField()
    name = models.CharField(max_length=32)


    class Meta:
        verbose_name = "cronjob content"
        verbose_name_plural = 'cronjob content'

    def __str__(self):
        return self.name