from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel

class CustomerBase(SQLModel):
  name: str
  description: str | None
  email: EmailStr
  age: int

class Customer(CustomerBase, table=True):
  id: int | None = None

class Customer_create(CustomerBase):
  pass