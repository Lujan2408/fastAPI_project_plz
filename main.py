from fastapi import FastAPI
from models.customer import Customer_create, Customer, Customer_update
from models.transaction import Transaction, Invoice
from db import SessionDependency, create_db_and_tables
from sqlmodel import select, update
from fastapi import HTTPException, status

app = FastAPI(lifespan=create_db_and_tables)

#  This is a list of customers supposed to be a database
db_customers: list[Customer] = []

# Get methods ⬇️

@app.get("/customers", response_model=list[Customer])
async def list_customers(session: SessionDependency):
  return session.exec(select(Customer)).all()
  
@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer_by_id(customer_id: int, session: SessionDependency):
  customer_db = session.get(Customer, customer_id)
  if not customer_db: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found or does not exist")
  return customer_db

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

# Patch methods ⬇️
@app.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def update_customer(customer_id: int, customer: Customer_update, session: SessionDependency): 
  customer_db = session.get(Customer, customer_id)
  if not customer_db: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found or does not exist")
  customer_data = customer.model_dump(exclude_unset=True)
  customer_db.sqlmodel_update(customer_data)
  session.add(customer_db)
  session.commit()
  session.refresh(customer_db)
  return customer_db

# Delete methods ⬇️

@app.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int, session: SessionDependency): 
  customer_db = session.get(Customer, customer_id)
  if not customer_db: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found or does not exist")
  
  session.delete(customer_db)
  session.commit()
  return {"detail": "Customer deleted successfully"}