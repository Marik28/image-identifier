import redis as r

from settings import settings

redis = r.Redis(
    settings.redis_host,
    settings.redis_port,
    settings.redis_db,
    decode_responses=True)


def get_redis():
    return redis
