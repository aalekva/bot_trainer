from sqlmodel import Session, select
from database import engine
from models import Client, Trainer, Schedule, Booking
from datetime import datetime


# =================== Clients ===================
def get_all_clients() -> list[Client]:
    with Session(engine) as session:
        return session.exec(select(Client)).all()

def get_client_by_id(client_id: int) -> Client | None:
    with Session(engine) as session:
        return session.get(Client, client_id)

# =================== Trainers ===================
def get_all_trainers() -> list[Trainer]:
    with Session(engine) as session:
        return session.exec(select(Trainer)).all()

def get_trainer_by_id(trainer_id: int) -> Trainer | None:
    with Session(engine) as session:
        return session.get(Trainer, trainer_id)

# =================== Schedule ===================
def get_trainer_schedule(trainer_id: int, only_free: bool = True) -> list[Schedule]:
    with Session(engine) as session:
        query = select(Schedule).where(Schedule.trainer_id == trainer_id)
        if only_free:
            query = query.where(Schedule.status == "free")
        return session.exec(query).all()

def get_slot_by_id(slot_id: int) -> Schedule | None:
    with Session(engine) as session:
        return session.get(Schedule, slot_id)

def create_slot(trainer_id: int, slot_timestamp: datetime) -> Schedule:
    with Session(engine) as session:
        slot = Schedule(trainer_id=trainer_id, slot_timestamp=slot_timestamp, status="free")
        session.add(slot)
        session.commit()
        session.refresh(slot)
        return slot

def update_slot(slot_id: int, slot_timestamp: datetime | None = None, status: str | None = None) -> Schedule | None:
    with Session(engine) as session:
        slot = session.get(Schedule, slot_id)
        if not slot or (slot.status != "free" and status == "free"):
            return None
        if slot_timestamp:
            slot.slot_timestamp = slot_timestamp
        if status:
            slot.status = status
        session.add(slot)
        session.commit()
        session.refresh(slot)
        return slot

def delete_slot(slot_id: int) -> bool:
    with Session(engine) as session:
        slot = session.get(Schedule, slot_id)
        if not slot or slot.status != "free":
            return False
        session.delete(slot)
        session.commit()
        return True

# =================== Bookings ===================
def get_bookings_by_trainer(trainer_id: int) -> list[Booking]:
    with Session(engine) as session:
        return session.exec(select(Booking).where(Booking.trainer_id == trainer_id)).all()

def get_bookings_with_clients() -> list[Booking]:
    with Session(engine) as session:
        return session.exec(select(Booking)).all()

def get_bookings_by_client(client_id: int) -> list[Booking]:
    with Session(engine) as session:
        return session.exec(select(Booking).where(Booking.client_id == client_id)).all()

def create_booking(data) -> Booking:
    with Session(engine) as session:
        slot = session.get(Schedule, data.slot_id)
        if not slot or slot.status != "free":
            return None
        booking = Booking(
            client_name=data.client_name,
            client_phone=data.client_phone,
            trainer_id=data.trainer_id,
            slot_id=data.slot_id,
            status="active"
        )
        slot.status = "booked"
        session.add(slot)
        session.add(booking)
        session.commit()
        session.refresh(booking)
        return booking

def cancel_booking(booking_id: int) -> bool:
    with Session(engine) as session:
        booking = session.get(Booking, booking_id)
        if not booking or booking.status != "active":
            return False
        booking.status = "cancelled"
        slot = session.get(Schedule, booking.slot_id)
        slot.status = "free"
        session.add(slot)
        session.add(booking)
        session.commit()
        return True

def move_booking(booking_id: int, new_slot_id: int) -> Booking | None:
    with Session(engine) as session:
        booking = session.get(Booking, booking_id)
        new_slot = session.get(Schedule, new_slot_id)
        if not booking or not new_slot or new_slot.status != "free":
            return None
        old_slot = session.get(Schedule, booking.slot_id)
        old_slot.status = "free"
        new_slot.status = "booked"
        booking.slot_id = new_slot_id
        session.add(old_slot)
        session.add(new_slot)
        session.add(booking)
        session.commit()
        session.refresh(booking)
        return booking
   
