from pydantic import BaseModel

class UserDto(BaseModel):
    firstName:str
    lastName:str
    city:str
    age:int
    active:bool=True
