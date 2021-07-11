from pydantic import BaseSettings


class Setting(BaseSettings):
    server_host: str = 'localhost'
    server_port: int = 5000
    debug: bool = True

    redis_db: int = 0
    redis_host: str = 'localhost'
    redis_port: int = 6379
    inappropriate_images_set_name: str = "inappropriate_images"
    images_set_name: str = "images"

    database_url = "sqlite:///./images.db"

    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600

    username_min_len: int = 5
    username_max_len: int = 30


settings = Setting(_env_file='.env')
