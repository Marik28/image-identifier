from fastapi import Depends
from redis import Redis

from redis_utils import get_redis


class ImagesService:

    def __init__(self,
                 redis: Redis = Depends(get_redis),
                 ):
        self.redis = redis

    def get_random_image(self):
        pass
