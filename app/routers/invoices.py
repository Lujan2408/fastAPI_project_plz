from fastapi import APIRouter
from models.invoices import Invoice

router = APIRouter(prefix="/invoices", tags=["invoices"])

@router.post("")
async def create_invoice(invoice_data: Invoice): 
  return invoice_data