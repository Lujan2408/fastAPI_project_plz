from pydantic import BaseModel

class Customer(BaseModel):
  name: str
  description: str | None
  email: str
  age: int