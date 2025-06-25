from fastapi import FastAPI
from models.customer import Customer_create, Customer
from models.transaction import Transaction, Invoice
from db import SessionDependency, create_db_and_tables
from sqlmodel import select

app = FastAPI(lifespan=create_db_and_tables)

#  This is a list of customers supposed to be a database
db_customers: list[Customer] = []

# Get methods ⬇️

@app.get("/customers", response_model=list[Customer])
async def list_customers(session: SessionDependency):
  return session.exec(select(Customer)).all()
  
@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer_by_id(id: int):
  customer = next((customer for customer in db_customers if customer.id == id), None)
  return customer

# Post methods ⬇️

@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: Customer_create, session: SessionDependency): 
  # Validate the customer data using the Customer model, inside we pass a dictionary
  customer = Customer.model_validate(customer_data.model_dump())
  session.add(customer)
  session.commit()
  session.refresh(customer)
  return customer

@app.post("/transactions")
async def create_transaction(transaction_data: Transaction):  
  return transaction_data

@app.post("/invoices")
async def create_invoice(invoice_data: Invoice): 
  return invoice_data