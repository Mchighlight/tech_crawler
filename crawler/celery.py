from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


QUEUE_JOBS = 'job'
QUEUE_CRONJOBS = 'cronjob'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawler.settings')

app = Celery('crawler')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('testing, testing ,testing')
