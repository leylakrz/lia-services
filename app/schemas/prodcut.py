from typing import List, Optional

from pydantic import BaseModel

from app.models import Product


class ProductRequest(BaseModel):
    name: str
    price: float
    description: str


class ProductRequestUpdate(BaseModel):
    name: Optional[str]
    price: Optional[float]
    description: Optional[str]


class ProductResponseList(BaseModel):
    data: List[Product]
