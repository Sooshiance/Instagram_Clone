from django.utils import timezone

from celery import shared_task

from .models import Story


@shared_task
def hide_expired_stories():
    cutoff_time = timezone.now() - timezone.timedelta(seconds=86400)
    
    stories_to_hide = Story.objects.filter(is_visible=True, is_archived=False, created_at__lte=cutoff_time)
    
    stories_to_hide.update(is_visible=False, hidden=True)
