from fastapi import FastAPI
from fastapi.routing import APIRouter

from config import log
from src.router import routes

app = FastAPI(
    title="API Animal Registration System",
    description="API для работы с базой MongoDB"
)

app.include_router(APIRouter(routes=routes))


@app.on_event("startup")
async def startup() -> None:
    log.info('Запуск приложение')


@app.on_event("shutdown")
async def shutdown() -> None:
    log.info('Завершение работы приложения')


@app.get('/ping', tags=['Test API'])
async def get_ping_pong() -> dict:
    """Функция для проверки, что API доступен"""
    log.info(f'Проверка работы API {get_ping_pong.__name__}')
    return {"ping": "pong"}
