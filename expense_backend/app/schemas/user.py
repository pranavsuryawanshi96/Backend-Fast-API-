from pydantic import BaseModel, Field


class UserRequestDTO(BaseModel):

    name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    email: str = Field(
        ...,
        min_length=5
    )

    age: int = Field(
        ...,
        gt=0
    )

    is_active: bool = True


class UserResponseDTO(BaseModel):

    id: int
    name: str
    email: str
    age: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }