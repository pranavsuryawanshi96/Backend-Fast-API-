class UserRepository:
    def find_by_email(self,email:str):
        pass

    def save(self,user):
        pass

def get_users():
    query="select * from users"
    users=[]
    return users