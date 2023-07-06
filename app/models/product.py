from beanie import Document
from pydantic import BaseModel as PydanticBaseModel

from app.utils.exceptions import NotFoundException


class Product(Document):
    name: str
    price: float
    description: str

    class Settings:
        name = "product"

    @classmethod
    async def list(cls):
        return await cls.all().to_list()

    @classmethod
    async def add(cls, info: PydanticBaseModel):
        new_obj = Product(**info.dict())
        await new_obj.insert()
        return new_obj

    @classmethod
    async def get_or_404(cls, *args, **kwargs):
        obj = await cls.get(*args, **kwargs)
        if obj:
            return obj
        raise NotFoundException

    @classmethod
    async def partial_update_or_404(cls, obj_id, info: PydanticBaseModel):
        obj = await Product.get_or_404(obj_id)
        await obj.set(info.dict(exclude_unset=True))
        return obj

    @classmethod
    async def delete_or_404(cls, obj_id):
        obj = await Product.get_or_404(obj_id)
        await obj.delete()
