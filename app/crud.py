from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas


async def create_query(
    db: AsyncSession,
    data: schemas.QueryRequest,
    result: bool
):
    """Создание новой записи в базе данных."""
    existing_query = await db.execute(
        select(models.QueryHistory).where(
            models.QueryHistory.cadastral_number == data.cadastral_number
        )
    )
    if existing_query.scalars().first() is not None:
        raise ValueError("Запись с таким кадастровым номером уже существует.")

    query = models.QueryHistory(
        cadastral_number=data.cadastral_number,
        latitude=data.latitude,
        longitude=data.longitude,
        result=result
    )
    db.add(query)
    await db.commit()


async def get_all_history(db: AsyncSession):
    """Получение списка всех записей из базы данных."""
    result = await db.execute(select(models.QueryHistory))
    return result.scalars().all()


async def get_history_by_cadastral_number(
    db: AsyncSession,
    cadastral_number: str
):
    """Получение записи по кадастровому номеру."""
    result = await db.execute(
        select(models.QueryHistory).where(
            models.QueryHistory.cadastral_number == cadastral_number
        )
    )
    return result.scalars().all()
