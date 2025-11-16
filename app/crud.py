from sqlalchemy.orm import Session
from . import models, schemas, auth
from typing import List

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user_in: schemas.UserCreate, role: str = "customer"):
    hashed = auth.get_password_hash(user_in.password)
    user = models.User(
        email=user_in.email,
        hashed_password=hashed,
        full_name=user_in.full_name,
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Restaurants
def create_restaurant(db: Session, rest_in: schemas.RestaurantCreate):
    r = models.Restaurant(**rest_in.dict())
    db.add(r)
    db.commit()
    db.refresh(r)
    return r

def list_restaurants(db: Session, skip=0, limit=100) -> List[models.Restaurant]:
    return db.query(models.Restaurant).offset(skip).limit(limit).all()

# Menu items
def create_menu_item(db: Session, item_in: schemas.MenuItemCreate):
    item = models.MenuItem(**item_in.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def list_menu_items(db: Session, restaurant_id: int = None):
    q = db.query(models.MenuItem)
    if restaurant_id:
        q = q.filter(models.MenuItem.restaurant_id == restaurant_id)
    return q.all()

# Orders
def create_order(db: Session, user: models.User, order_in: schemas.OrderCreate):
    order = models.Order(user_id=user.id, status=models.OrderStatus.pending)
    db.add(order)
    db.flush()  # get order.id
    total = 0.0
    for it in order_in.items:
        menu_item = db.query(models.MenuItem).filter(models.MenuItem.id == it.menu_item_id).first()
        if not menu_item:
            raise ValueError(f"Menu item {it.menu_item_id} not found")
        price = menu_item.price
        oi = models.OrderItem(order_id=order.id, menu_item_id=menu_item.id, quantity=it.quantity, price=price)
        db.add(oi)
        total += price * it.quantity
    order.total_amount = total
    db.commit()
    db.refresh(order)
    return order

# def get_orders_for_user(db: Session, user: models.User):
#     return db.query(models.Order).filter(models.Order.user_id == user.id).all()
def get_all_orders(db: Session):
    # Return all orders, no user required
    return db.query(models.Order).all()


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def update_order_status(db: Session, order: models.Order, status: str):
    order.status = status
    db.commit()
    db.refresh(order)
    return order
