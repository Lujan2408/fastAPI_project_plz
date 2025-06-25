from fastapi import FastAPI
from models.customer import Customer
from models.transaction import Transaction, Invoice

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello"}

@app.post("/customers")
async def create_customer(customer_data: Customer): 
  return customer_data

@app.post("/transactions")
async def create_transaction(transaction_data: Transaction):  
  return transaction_data

@app.post("/invoices")
async def create_invoice(invoice_data: Invoice): 
  return invoice_data