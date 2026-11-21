from fastapi import APIRouter, HTTPException,Path,Query,status
from pydantic import BaseModel,Field
from typing import Annotated

router = APIRouter(prefix="/items", tags=["items"])
fake_db = {
    1: {"name": "Foo", "price": 50.2},
    2: {"name": "Bar", "price": 20.0}
    }

class Item(BaseModel):
    name: str = Field(..., title="Название", example="Телефон")
    price: float = Field(..., gt=0, title="Цена", example=199.99)
    is_offer: bool | None = Field(None, title="Акционный товар")

@router.get("/{item_id}")
def read_item(
    item_id: int = Path(..., title="ID товара", ge=1),
    q: str | None = Query(None, title="Поисковый запрос", max_length=50)
    ):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": fake_db[item_id], "q": q}

@router.post("/", response_model=Item)
def create_item(item: Item):
    return item

@router.put("/{item_id}")
def update_item(
    item_id: Annotated[int, Path(title="ID товара", ge=1)],
    item: Item,
    ):
    if item_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            )

    for other_id, existing_item in fake_db.items():
        if other_id != item_id and existing_item["name"].lower() == item.name.lower():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Товар с именем '{item.name}' уже существует",
                )

    fake_db[item_id] = item.model_dump()
    return {"item_id": item_id, "item": fake_db[item_id]}