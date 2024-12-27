from datetime import datetime, time

from celery import shared_task


@shared_task
def reset_clock() -> bool:
    if datetime.now() == time(hour=24, minute=0, second=0, tzinfo="UTC"):
        return True
    return False
