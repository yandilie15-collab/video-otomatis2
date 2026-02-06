
from pathlib import Path
from app.celery_app import celery_app
from app.subtitle.generator import generate_srt
from app.video.youtube import burn_subtitle

@celery_app.task
def add_subtitle(video_path:str, text:str):
    video = Path(video_path)
    srt = video.with_suffix(".srt")
    generate_srt(text, srt)
    return str(burn_subtitle(video, srt))
