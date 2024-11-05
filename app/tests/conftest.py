import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal


@pytest.fixture(scope="module")
def client():
    """Фикстура для тест-клиента."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function", autouse=True)
async def db():
    """Асинхронная фикстура для работы с основной базой данных."""
    async with SessionLocal() as session:
        yield session
        await session.close()