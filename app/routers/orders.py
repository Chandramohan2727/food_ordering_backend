from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, deps, models

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=schemas.OrderOut)
def place_order(order_in: schemas.OrderCreate, db: Session = Depends(deps.get_db), current_user=Depends(deps.get_current_user)):
    try:
        order = crud.create_order(db, current_user, order_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    # return with nested items - note: OrderOut expects items; ensure relationships loaded
    return order

@router.get("/", response_model=list[schemas.OrderOut])
def get_my_orders(db: Session = Depends(deps.get_db)):
    return crud.get_all_orders(db)

@router.patch("/{order_id}/status", response_model=schemas.OrderOut)
def update_status(order_id: int, status: models.OrderStatus, db: Session = Depends(deps.get_db)):
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(404, "Order not found")
    return crud.update_order_status(db, order, status)
