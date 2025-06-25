from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo
from models.customer import Customer

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello"}

country_timezones = {
  "CO": "America/Bogota",
  "MX": "America/Mexico_City",
  "AR": "America/Buenos_Aires",
  "BR": "America/Sao_Paulo",
  "CL": "America/Santiago",
  "PE": "America/Lima",
  "EC": "America/Guayaquil",
}

@app.get("/time/{iso_code}")
async def get_time(iso_code: str):
  iso = iso_code.upper()
  timezone_str = country_timezones.get(iso)
  tz = ZoneInfo(timezone_str)
  return {"Time": datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")}

@app.post("/customers")
async def create_customer(customer_data: Customer): 
  return customer_data