from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import minio_settings
from infrastructure import containers
from presentation.transcription.route import route as transcription_route

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
)
app.include_router(transcription_route)

minio_container = containers.MinIOContainer(
    endpoint_url=minio_settings.minio_endpoint_url,
    secret_key=minio_settings.minio_secret_key,
    access_key=minio_settings.minio_access_key,
)

rabbitmq_container = containers.RabbitMQContainer()

transcription_container = containers.TranscriptionContainer(
    bytes_storage_container=minio_container,
    message_broker_container=rabbitmq_container,
)
