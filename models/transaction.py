from sqlmodel import Relationship, SQLModel, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Customers.customer import Customer

class TransactionBase(SQLModel): 
  amount: int
  description: str

class Transaction(TransactionBase, table=True): 
  id: int | None = Field(default=None, primary_key=True)
  customer_id: int = Field(foreign_key="customer.id")
  customer: "Customer" = Relationship(back_populates="transactions")

class Transaction_create(TransactionBase):
  customer_id: int = Field(foreign_key="customer.id")