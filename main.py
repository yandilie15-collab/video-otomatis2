
from fastapi import FastAPI
from celery import chain
from app.tasks.render import render_youtube
from app.tasks.subtitle import add_subtitle
from app.tasks.upload_youtube import upload_youtube

app = FastAPI()

@app.post("/jobs/youtube")
def create_job():
    chain(
        render_youtube.s(1),
        add_subtitle.s("Ini contoh subtitle otomatis untuk video."),
        upload_youtube.s()
    ).delay()
    return {"status":"queued with subtitle"}
