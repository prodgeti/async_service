from pydantic import BaseModel


class QueryRequest(BaseModel):
    """Схема для данных запроса при создании записи."""
    cadastral_number: str
    latitude: float
    longitude: float


class QueryResult(BaseModel):
    """Схема для возврата результата обработки запроса."""
    result: bool


class QueryHistoryResponse(BaseModel):
    """Схема ответа с данными кадастровой записи."""
    cadastral_number: str
    latitude: float
    longitude: float
    result: bool

    class Config:
        from_attributes = True
