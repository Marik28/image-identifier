from typing import Optional

from database import database, Image
from redis_utils import redis
from settings import settings


def add_to_inappropriate(filename: str):
    """Добавляет картинку в список с несоответствующими картинками"""
    redis.sadd(settings.inappropriate_images_set_name, filename)


async def add_to_database(filename: str, liked: bool):
    """Добавляет понравившуюся/непонравившуюся картинку в базу"""
    # query = images.insert().values(filename=filename, liked=liked)
    # await database.execute(query)
    ...


def remove_image(filename: str):
    """Удаляет картинку из редиса"""
    redis.srem(settings.images_set_name, filename)


def get_random_image() -> Optional[str]:
    """Возвращает случайную картинку для анализа"""
    return redis.srandmember(settings.images_set_name)


def get_inappropriate_images():
    imgs = list(redis.smembers(settings.inappropriate_images_set_name))
    count = len(imgs)
    return {
        "count": count,
        "images": imgs
    }


async def get_images_info():
    query = f"""SELECT * FROM {Image.__tablename__};"""
    raw_images_list = await database.fetch_all(query)

    # all_images = images.select()
