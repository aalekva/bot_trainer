from fastapi import FastAPI
from database import create_db_and_tables
from routers import clients, trainers, bookings, schedule

app = FastAPI(title="Training Booking API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Подключаем роутеры
app.include_router(clients.router)
app.include_router(trainers.router)
app.include_router(bookings.router)
app.include_router(schedule.router)

@app.get("/")
def root():
    return {"message": "Training Booking API is running"}

@app.get("/status")
def status():
    return {"status": "ok", "api": "running"}
