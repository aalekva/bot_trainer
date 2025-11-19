from sqlmodel import select
from database import get_session
from models import Client, Trainer, Schedule, Booking

# ===== Клиенты =====
def get_all_clients():
    with get_session() as session:
        return session.exec(select(Client)).all()

def get_client_by_id(client_id: int):
    with get_session() as session:
        client = session.get(Client, client_id)
        return client

# ===== Тренеры =====
def get_all_trainers():
    with get_session() as session:
        return session.exec(select(Trainer)).all()

def get_trainer_schedule(trainer_id: int, only_free: bool = True):
    with get_session() as session:
        query = select(Schedule).where(Schedule.trainer_id == trainer_id)
        if only_free:
            query = query.where(Schedule.status == "free")
        return session.exec(query).all()

# ===== Бронирования =====
def get_bookings_by_trainer(trainer_id: int):
    with get_session() as session:
        query = select(Booking).where(Booking.trainer_id == trainer_id)
        return session.exec(query).all()

def get_bookings_with_clients():
    with get_session() as session:
        query = select(Booking).join(Client)
        return session.exec(query).all()
