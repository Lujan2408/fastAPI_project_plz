from sqlmodel import Session, create_engine, SQLModel
from typing import Annotated
from fastapi import Depends, FastAPI

from models.Customers.customer import Customer
from models.plans import Plan
from models.transaction import Transaction
from models.invoices import Invoice 

sqlite_file_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables(app: FastAPI): 
  # Create all tables in the database
  SQLModel.metadata.create_all(engine)
  yield


def get_session():
  # Context processor: Its a variable that allows us to use other variables from other classes
  with Session(engine) as session: # return a variable that we called "session"
    yield session

SessionDependency = Annotated[Session, Depends(get_session)]