from fastapi import FastAPI
from db import create_db_and_tables
from .routers.customers import router as customers_router
from .routers.transactions import router as transactions_router
from .routers.invoices import router as invoices_router

app = FastAPI(lifespan=create_db_and_tables)
app.include_router(customers_router)
app.include_router(transactions_router)
app.include_router(invoices_router)


