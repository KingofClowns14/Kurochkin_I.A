from fastapi import FastAPI,Request
from app.config import Settings
from app.routers import items
import logging,time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

settings = Settings()
app = FastAPI(
    title=settings.app_name,
    description="Лабораторная работа по FastAPI",
    version="1.0.0",
    contact={
        "name": "Курочкин Илья",
        "email": settings.admin_email,
    }
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logger.info("Входящий запрос: %s %s", request.method, request.url.path)
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(
        "Запрос завершён: %s %s -> статус %s (%.3f сек)",
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )
    return response

app.include_router(items.router)

@app.get("/")
def read_root():
    logger.info("Обращение к корневому маршруту /")
    return {"message": "Hello, FastAPI!"}

@app.get("/info")
def info():
    logger.info("Запрос информации о приложении /info")
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_page": settings.items_per_page,
    }