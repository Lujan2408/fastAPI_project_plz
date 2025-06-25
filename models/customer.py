from pydantic import BaseModel, EmailStr

class Customer(BaseModel):
  name: str
  description: str | None
  email: EmailStr
  age: int