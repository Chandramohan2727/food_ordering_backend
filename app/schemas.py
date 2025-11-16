from pydantic import BaseModel, EmailStr
from typing import Optional, List
from enum import Enum
import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    role: str

    # class Config:
    #     orm_mode = True
    model_config = {"from_attributes": True}


class RestaurantCreate(BaseModel):
    name: str
    description: Optional[str] = None
    address: Optional[str] = None

class RestaurantOut(RestaurantCreate):
    id: int
    # class Config:
    #     orm_mode = True
    model_config = {"from_attributes": True}

class MenuItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    restaurant_id: int

class MenuItemOut(MenuItemCreate):
    id: int
    # class Config:
    #     orm_mode = True
    model_config = {"from_attributes": True}

class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderItemOut(BaseModel):
    id: int
    menu_item_id: int
    quantity: int
    price: float
    # class Config:
    #     orm_mode = True
    model_config = {"from_attributes": True}

class OrderOut(BaseModel):
    id: int
    user_id: int
    created_at: datetime.datetime
    status: str
    total_amount: float
    items: List[OrderItemOut]
    # class Config:
    #     orm_mode = True
    model_config = {"from_attributes": True}
