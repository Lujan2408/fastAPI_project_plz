from pydantic import BaseModel
from models.customer import Customer

class Transaction(BaseModel): 
  id: int
  amount: int
  description: str

class Invoice(BaseModel): 
  id: int
  customer: Customer
  transactions: list[Transaction]
  total_amount: int

  @property
  def total_amount(self):
    return sum(transaction.amount for transaction in self.transactions) 