from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.schemas.api_response import ApiResponse
from app.schemas.expense import ExpenseRequestDto, ExpenseResponseDTO 
from app.models.expense import Expense

expense_router=APIRouter(
    prefix="/expenses"
)

# create expense
@expense_router.post("/",response_model=ApiResponse)
def create_expense(expense_request_dto:ExpenseRequestDto,db:Session=Depends(get_db)):
    # create a new expense import from models
    new_expense=Expense(
        title=expense_request_dto.title,
        description=expense_request_dto.description,
        amount= expense_request_dto.amount
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    print("new expense is created")
    return ApiResponse(status="success",message="Expense is created successfully",data={"expense":ExpenseResponseDTO.model_validate(new_expense)})



# get all expenses




# get expense by id


# update expense by id


# delete expense by id

# search expense by title

