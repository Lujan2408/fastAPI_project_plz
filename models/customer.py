from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.transaction import Transaction

class CustomerBase(SQLModel):
  name: str 
  description: str | None = Field(default=None)
  email: EmailStr
  age: int 

class Customer(CustomerBase, table=True):
  id: int | None = Field(default=None, primary_key=True)
  transactions: list["Transaction"] = Relationship(back_populates="customer")

class Customer_create(CustomerBase):
  pass

class Customer_update(CustomerBase): 
  name: str | None = None
  description: str | None = None
  email: EmailStr | None = None
  age: int | None = None
