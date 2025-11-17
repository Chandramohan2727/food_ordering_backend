from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.deps import get_db, get_current_user

router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"]
)

# Create restaurant (any logged-in user)
@router.post("/", response_model=schemas.RestaurantOut)
def create_restaurant(
    restaurant: schemas.RestaurantCreate,
    db: Session = Depends(get_db),
    # current_user = Depends(get_current_user)  # JWT required
):
    return crud.create_restaurant(db, restaurant)

# List restaurants (public)
@router.get("/", response_model=List[schemas.RestaurantOut])
def list_restaurants(db: Session = Depends(get_db)):
    return crud.get_restaurants(db)
