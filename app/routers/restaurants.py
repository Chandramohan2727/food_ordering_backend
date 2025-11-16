# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from .. import schemas, crud, deps

# router = APIRouter(prefix="/restaurants", tags=["restaurants"])

# @router.post("/", response_model=RestaurantOut)
# async def create_restaurant(current_user: User = Depends(get_current_user)):
#     # No admin check — any logged-in user can create
#     return {"id": 1, "name": "My Restaurant", "location": "City"}


# @router.get("/", response_model=list[schemas.RestaurantOut])
# def list_restaurants(db: Session = Depends(deps.get_db)):
#     return crud.list_restaurants(db)
# app/routers/restaurants.py

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List

# from app import schemas, models, crud
# # from app.database import get_db
# from app.deps import get_db, get_current_user

# from app.deps import get_current_user

# router = APIRouter(
#     prefix="/restaurants",
#     tags=["restaurants"]
# )

# # Create a restaurant (any logged-in user)
# @router.post("/", response_model=schemas.RestaurantOut)
# def create_restaurant(
#     restaurant: schemas.RestaurantCreate,
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(get_current_user)
# ):
#     # Simply create the restaurant; no admin check
#     db_restaurant = crud.create_restaurant(db, restaurant)
#     return db_restaurant

# # Get all restaurants
# @router.get("/", response_model=List[schemas.RestaurantOut])
# def list_restaurants(db: Session = Depends(get_db)):
#     restaurants = crud.get_restaurants(db)
#     return restaurants

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
