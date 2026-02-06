
from celery import Celery
import os
REDIS_URL = os.getenv("REDIS_URL","redis://redis:6379/0")
celery_app = Celery("avf", broker=REDIS_URL, backend=REDIS_URL)
celery_app.conf.update(task_track_started=True, task_acks_late=True, worker_prefetch_multiplier=1)
