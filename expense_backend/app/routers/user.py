from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.users import User
from app.schemas.user import UserRequestDTO, UserResponseDTO
from app.schemas.api_response import ApiResponse


user_router = APIRouter(
    prefix="/users"

)

@user_router.post("/", response_model=ApiResponse)
def create_user(
    user_request_dto: UserRequestDTO,
    db: Session = Depends(get_db)
):

    new_user = User(
        name=user_request_dto.name,
        email=user_request_dto.email,
        age=user_request_dto.age,
        is_active=user_request_dto.is_active
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return ApiResponse(
        status="success",
        message="User created successfully",
        data={
            "user": UserResponseDTO.model_validate(new_user)
        }
    )

@user_router.get("/", response_model=ApiResponse)
def get_all_users(
    db: Session = Depends(get_db)
):

    users = db.query(User).all()

    return ApiResponse(
        status="success",
        message="Users retrieved successfully",
        data={
            "users": [
                UserResponseDTO.model_validate(user)
                for user in users
            ]
        }
    )

@user_router.get("/{user_id}", response_model=ApiResponse)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return ApiResponse(
        status="success",
        message="User retrieved successfully",
        data={
            "user": UserResponseDTO.model_validate(user)
        }
    )

@user_router.get("/{user_id}", response_model=ApiResponse)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return ApiResponse(
        status="success",
        message="User retrieved successfully",
        data={
            "user": UserResponseDTO.model_validate(user)
        }
    )

@user_router.put("/{user_id}", response_model=ApiResponse)
def update_user(
    user_id: int,
    user_request_dto: UserRequestDTO,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    user.name = user_request_dto.name
    user.email = user_request_dto.email
    user.age = user_request_dto.age
    user.is_active = user_request_dto.is_active

    db.commit()
    db.refresh(user)

    return ApiResponse(
        status="success",
        message="User updated successfully",
        data={
            "user": UserResponseDTO.model_validate(user)
        }
    )   