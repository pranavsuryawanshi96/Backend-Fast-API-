from fastapi  import FastAPI,Depends,status,HTTPException
from .schemas.api import ApiResponse
from .schemas.user import UserDto
from .routers.auth import auth_router
from .routers.user import user_router

# create a object
app=FastAPI(
    title="Backend FastAPi...",
    description="This is just tut",
    version="1.0"
)

app.include_router(auth_router)
app.include_router(user_router)

@app.get("/")
def root():
    print("this is root api")
    return{
        "message":"Backend Server is Fine"
    }

def get_token():
    print("getting token")
    return "token_aaadawf"
#  create a function 
# @app.get("/",response_model=ApiResponse)
# def home():
#     print("Its working")
#     return ApiResponse(message="Hey this is working fine", success=True, status="Ok")

# @app.post("/users")
# def create_user():
#     print("creating user")
#     return ApiResponse(
#         message="created new user successfully",
#         status="Ok",
#         success=True
#     )

# @app.get("/users/search")
# def search_user(firstName:str="",lastName:str=""):
#     print(firstName,lastName)
#     print("searching users")
#     return {
#         "data":[],
#         "success":True

#     }

# @app.put("/users/{user_id}/name/{user_name}")
# def update_user(user_id:int,user_name:str):
#     print("update user")
#     print("user name", user_name)
#     print("user id",user_id)
#     return {
#         "message":"user updated",
#         "user_name":user_name,
#         "user_id":user_id
#     }

# @app.post("/users",status_code=status.HTTP_201_CREATED)
# def create_user(users:UserDto, token=Depends(get_token)):
#     if users.firstName=="abc":
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="This user is not allowed try another first name"
#         )
#     print("firstName",users.firstName)
#     print("lastName",users.lastName)
#     return{
#         "message":"user created successfully",
#         "user":users,
#         "token":token
#     }


# @app.get("/get-users")
# def get_users():
#     print("getting all users")
#     return [
#         "pranav",
#         "patil",
#     ]