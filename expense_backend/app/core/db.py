from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./expense.db"



# create engine
engine=create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread":False
    }
)


# sessional
LocalSession= sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# dependency 

# Dependency
# This function used by fast api
def get_db():
    db = LocalSession()

    try:
        # This gives the session to the fast api    
        yield db
    finally:
        # always executed:db should close always imp
        db.close()


Base= declarative_base()