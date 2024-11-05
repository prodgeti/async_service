from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import SessionLocal
import random

app = FastAPI()


async def get_db():
    """Асинхронное подключение к базе данных."""
    async with SessionLocal() as session:
        yield session


@app.get("/ping")
async def ping():
    """Проверка статуса сервера."""
    return {"status": "Server is running"}


@app.post("/query", response_model=schemas.QueryResult)
async def query(
    data: schemas.QueryRequest,
    db: AsyncSession = Depends(get_db)
):
    """Создание новой кадастровой записи."""
    result = random.choice([True, False])
    try:
        await crud.create_query(db, data, result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"result": result}


@app.get("/history", response_model=list[schemas.QueryHistoryResponse])
async def history(db: AsyncSession = Depends(get_db)):
    """Получение всех кадастровых записей."""
    return await crud.get_all_history(db)


@app.get(
    "/history/{cadastral_number}",
    response_model=list[schemas.QueryHistoryResponse]
)
async def history_by_cadastral(
    cadastral_number: str,
    db: AsyncSession = Depends(get_db)
):
    """Получение записи по кадастровому номеру."""
    return await crud.get_history_by_cadastral_number(db, cadastral_number)


@app.get("/result", response_model=schemas.QueryResult)
async def result_emulator():
    """Возвращает случайный результат (пример ответа сервера)."""
    return {"result": random.choice([True, False])}
