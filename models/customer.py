from pydantic import BaseModel, EmailStr

class CustomerBase(BaseModel):
  name: str
  description: str | None
  email: EmailStr
  age: int

class Customer(CustomerBase):
  id: int | None = None

class Customer_create(CustomerBase):
  pass