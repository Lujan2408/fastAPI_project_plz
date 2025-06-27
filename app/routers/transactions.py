from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from db import SessionDependency
from models.customer import Customer
from models.transaction import Transaction, Transaction_create

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.get("", response_model=list[Transaction]) 
async def get_transactions(session: SessionDependency):
  return session.exec(select(Transaction)).all()

@router.post("", response_model=Transaction, status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction_data: Transaction_create, session: SessionDependency):
  transaction_data_dict = transaction_data.model_dump()
  customer = session.get(Customer, transaction_data_dict.get("customer_id"))
  if not customer: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found or does not exist")
  
  transaction_db = Transaction.model_validate(transaction_data_dict)
  session.add(transaction_db)
  session.commit()
  session.refresh(transaction_db)

  return transaction_db
