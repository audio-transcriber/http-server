from pydantic_settings import BaseSettings


class MinIOSettings(BaseSettings):
    minio_endpoint_url: str
    minio_access_key: str
    minio_secret_key: str

    class Config:
        env_file = '.env'


minio_settings = MinIOSettings()
