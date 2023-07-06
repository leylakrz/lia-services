from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.models import Product
from app.schemas.prodcut import ProductResponseList, ProductRequest, ProductRequestUpdate
from app.utils.decorators import handle_not_found

product_router = APIRouter(prefix="/product", tags=["product"])


@product_router.get("/", response_model=ProductResponseList)
async def list_products():
    return ProductResponseList(data=await Product.list())


@product_router.post("/", response_model=Product)
async def create_product(product: ProductRequest):
    return await Product.add(product)


@product_router.get("/{product_id}/", response_model=Product)
@handle_not_found
async def get_product_by_id(product_id: str):
    return await Product.get_or_404(product_id)


@product_router.patch("/{product_id}/", response_model=Product)
@handle_not_found
async def update_product(product_id: str, product: ProductRequestUpdate):
    return await Product.partial_update_or_404(product_id, product)


@product_router.delete("/{product_id}/", response_class=JSONResponse)
@handle_not_found
async def delete_product(product_id: str):
    await Product.delete_or_404(product_id)
    return {"message": "با موفقیت حذف شد."}