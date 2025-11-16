from fastapi import FastAPI
from .database import Base, engine
# from . import models
from .routers import users, restaurants, menu, orders

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Food Ordering Backend")

app.include_router(users.router)
app.include_router(restaurants.router)
app.include_router(menu.router)
app.include_router(orders.router)

@app.get("/")
def health():
    return {"status": "ok"}
