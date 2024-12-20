import os

from backend.settings.base import DEBUG

from celery import Celery


# Set the default Django settings module for the 'celery' program.
if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.develop")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.production")


app = Celery("django_celery")


# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
