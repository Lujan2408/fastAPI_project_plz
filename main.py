from fastapi import FastAPI
from models.customer import Customer_create, Customer
from models.transaction import Transaction, Invoice
from db import SessionDependency, create_db_and_tables

app = FastAPI(lifespan=create_db_and_tables)

#  This is a list of customers supposed to be a database
db_customers: list[Customer] = []

# Get methods ⬇️

@app.get("/customers", response_model=list[Customer])
async def list_customers():
  return db_customers

@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer_by_id(id: int):
  customer = next((customer for customer in db_customers if customer.id == id), None)
  return customer

# Post methods ⬇️

@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: Customer_create, session: SessionDependency): 
  # Validate the customer data using the Customer model, inside we pass a dictionary
  customer = Customer.model_validate(customer_data.model_dump())
  #  Assumming that this is a database, we need to increment the id
  customer.id = len(db_customers) 
  db_customers.append(customer) # append allows us to add the customer to the database
  return customer

@app.post("/transactions")
async def create_transaction(transaction_data: Transaction):  
  return transaction_data

@app.post("/invoices")
async def create_invoice(invoice_data: Invoice): 
  return invoice_data