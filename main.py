from fastapi import FastAPI
from fastapi import status
from fastapi import Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api import router
from database import database
from models.images import Decision
from settings import settings
from utils import add_to_inappropriate, add_to_database, get_random_image, get_inappropriate_images, remove_image, \
    get_images_info

app = FastAPI(debug=settings.debug)
origins = [
    "http://localhost:5000",
    "http://localhost:8080",
    "http://192.168.0.105:8080",
    "http://192.168.0.255:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/api/random-image/')
async def process_get_random_image():
    """Возвращает случайную картинку. Если картинок больше нет, то возвращает null"""
    image = get_random_image()
    return {'image': image}


@app.post('/api/decide/')
async def process_decide(decision: Decision):
    """Добавляет картинку в базу данных"""
    filename = decision.filename
    remove_image(filename)
    if not decision.appropriate:
        add_to_inappropriate(filename)
    else:
        await add_to_database(filename, decision.liked)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get("/api/inappropriate-images/")
def get_inappropriate_images_list():
    """Возвращает список со всеми неподходящими картинками"""
    return get_inappropriate_images()


# todo рофлан
@app.get("/api/images/")
async def get_images():
    return await get_images_info()


if __name__ == '__main__':
    uvicorn.run('main:app', reload=False, port=settings.server_port)
