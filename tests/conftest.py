import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from tortoise import Tortoise

from src.db import TEST_DATABASE_URL
from src.main import app


@pytest.fixture(scope='session', autouse=True)
async def init_db():
    await Tortoise.init(db_url=TEST_DATABASE_URL, modules={
        'models': ['src.insurance.models']
    })
    await Tortoise.generate_schemas()
    # yield
    # await Tortoise._drop_databases()


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
