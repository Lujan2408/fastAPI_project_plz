from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field

class CustomerBase(SQLModel):
  name: str 
  description: str | None = Field(default=None)
  email: EmailStr
  age: int 

class Customer(CustomerBase, table=True):
  id: int | None = Field(default=None, primary_key=True)

class Customer_create(CustomerBase):
  pass