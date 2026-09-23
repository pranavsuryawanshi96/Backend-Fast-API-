from fastapi import FastAPI
from app.core.db import Base, engine
import app.models.users
import app.models.expense
from app.routers.expense import expense_router

# Create tables
Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(expense_router)

@app.get("/")
def root():
    return{"message":"Hello World"}