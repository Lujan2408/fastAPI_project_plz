from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from models.Customers.customer_plan import Customer_plan

if TYPE_CHECKING: 
  from models.customer import Customer

class Plan(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  price: int
  description: str
  customers: list["Customer"] = Relationship(
    back_populates="plans",
    link_model=Customer_plan
  )
