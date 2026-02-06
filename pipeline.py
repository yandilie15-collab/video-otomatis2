
from uploader import upload_all
from analytics import log_view

def process_video(script, voice):
    video=f"video_{voice}.mp4"
    upload_all(video)
    log_view(video)
