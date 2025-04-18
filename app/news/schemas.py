from pydantic import BaseModel
from typing import Optional


class NewsAddSchem(BaseModel):
    title: str
    descriptions: str | None = None


class NewsReadSchem(BaseModel):
    id: int
    title: str
    descriptions: Optional[str] = None
