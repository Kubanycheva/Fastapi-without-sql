import fastapi
from pydantic import BaseModel
from datetime import datetime, date
mysite = fastapi.FastAPI(title='Test Project')


class Product(BaseModel):
    id: int
    product_name: str
    description: str
    price: int
    have: bool
    created_date: date | None

products = [
    {
        "id": 1,
        "product_name": "good",
        "description": "fine",
        "price": 2500,
        "have": True,
        "created_date": "2025-01-27"
    },
    {
        "id": 2,
        "product_name": "qwer",
        "description": "qwerty",
        "price": 2500,
        "have": True,
        "created_date": "2025-01-27"
    }
]


@mysite.get('/')
async def product_list():
    return products


@mysite.get('/{id}/')
async def product_detail(id: int):
    for i in products:
        if i["id"] == id:
            return i


@mysite.post('/')
async def product_create(pro: Product):
    products.append(pro)
    return products


@mysite.put('/{id}/')
async def product_update(id: int, pro: Product):
    for i in products:
        if i["id"] == id:
            i = pro
            return i


@mysite.delete('/{id}/')
async def product_delete(id: int):
    products.pop(id - 1)
    return products


