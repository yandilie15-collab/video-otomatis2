
from app.celery_app import celery_app
from app.video.youtube import render

@celery_app.task
def render_youtube(job_id:int):
    return str(render(job_id))
