#all  the api for users
from fastapi import APIRouter
user_router= APIRouter(prefix="/user")

@user_router.post("/")
def create_user():
    pass
@user_router.get("/")
def get_users():
    pass
@user_router.put("/")
def update_users():
    pass