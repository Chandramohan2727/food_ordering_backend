from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, deps, models

router = APIRouter(prefix="/menu", tags=["menu"])

@router.post("/", response_model=schemas.MenuItemOut)
def create_menu_item(item_in: schemas.MenuItemCreate, db: Session = Depends(deps.get_db)):
    # validate restaurant exists
    from ..models import Restaurant
    rest = db.query(Restaurant).filter(Restaurant.id == item_in.restaurant_id).first()
    if not rest:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return crud.create_menu_item(db, item_in)

@router.get("/", response_model=list[schemas.MenuItemOut])
def list_menu_items(restaurant_id: int | None = None, db: Session = Depends(deps.get_db)):
    return crud.list_menu_items(db, restaurant_id)
