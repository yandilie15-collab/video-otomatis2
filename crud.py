from sqlalchemy.orm import Session
from . import models

def create_job(db: Session, title: str):
    job = models.VideoJob(title=title)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

def get_jobs(db: Session):
    return db.query(models.VideoJob).all()
