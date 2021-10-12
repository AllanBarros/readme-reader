import os
from celery import Celery
from django.conf import settings
import django

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

django.setup()

app = Celery('api', include=['api.backend.views', 'api.backend.models', 'api.backend.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
