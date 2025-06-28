from sqlmodel import SQLModel, Field

class Customer_plan(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  plan_id: int = Field(foreign_key="plan.id", primary_key=True)
  customer_id: int = Field(foreign_key="customer.id", primary_key=True)