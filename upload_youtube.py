
from app.celery_app import celery_app
from app.settings import YOUTUBE_PRIVACY

@celery_app.task
def upload_youtube(path:str):
    print("Uploading with subtitle:", path)
    return "YT_DONE"
