from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.insurance.routers import insurance_router
from .db import DATABASE_URL

app = FastAPI()

app.include_router(insurance_router)

register_tortoise(
    app=app,
    db_url=DATABASE_URL,
    modules={'models': ['src.insurance.models']},
    generate_schemas=True,
    add_exception_handlers=True
)
