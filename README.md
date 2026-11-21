# Лабораторная работа №6. Введение в FastAPI

**Выполнил:** Курочкин Илья
**Стек:** Python, FastAPI, Uvicorn, Pydantic, pydantic-settings, uv

## Цель работы
Изучить основы разработки REST API с использованием фреймворка FastAPI: создание маршрутов, валидацию данных через Pydantic, модульную организацию через `APIRouter`, конфигурацию через переменные окружения, обработку ошибок, логирование и автоматическую документацию OpenAPI/Swagger.

## Структура проекта

```text
.
├── app/
│   ├── __init__.py
│   ├── config.py
│   └── routers/
│       ├── __init__.py
│       └── items.py
├── screenshots/
├── .env
├── .gitignore
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock