from sqlmodel import Session, create_engine
from typing import Annotated
from fastapi import Depends

sqlite_file_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def get_session():
  # Context processor: Its a variable that allows us to use other variables from other classes
  with Session(engine) as session: # return a variable that we called "session"
    yield session

SessionDependency = Annotated[Session, Depends(get_session)]