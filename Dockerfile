
FROM python:3.10-slim
RUN apt-get update && apt-get install -y ffmpeg
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn celery redis
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
