from fastapi import APIRouter
from models.transaction import Transaction

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("")
async def create_transaction(transaction_data: Transaction):  
  return transaction_data