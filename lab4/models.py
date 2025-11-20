from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

# ================================
# 1. Клиенты
# ================================
class Client(SQLModel, table=True):
    id_client: int = Field(primary_key=True)
    full_name: str
    phone: Optional[str] = None
    username: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

    bookings: List["Booking"] = Relationship(back_populates="client")

# ================================
# 2. Тренеры
# ================================
class Trainer(SQLModel, table=True):
    id_trainer: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    qualification: Optional[str] = None
    specialization: Optional[str] = None
    contacts: Optional[str] = None
    about: Optional[str] = None

    schedule: List["Schedule"] = Relationship(back_populates="trainer")
    bookings: List["Booking"] = Relationship(back_populates="trainer")

# ================================
# 3. Расписание (слоты)
# ================================
class Schedule(SQLModel, table=True):
    id_slot: Optional[int] = Field(default=None, primary_key=True)
    trainer_id: int = Field(foreign_key="trainer.id_trainer")
    slot_timestamp: datetime
    status: str = Field(default="free")

    trainer: Optional[Trainer] = Relationship(back_populates="schedule")
    booking: Optional["Booking"] = Relationship(back_populates="slot")

# ================================
# 4. Записи (бронирования)
# ================================
class Booking(SQLModel, table=True):
    id_booking: Optional[int] = Field(default=None, primary_key=True)
    client_id: int = Field(foreign_key="client.id_client")
    slot_id: int = Field(foreign_key="schedule.id_slot")
    status: str = Field(default="active")
    created_at: datetime = Field(default_factory=datetime.now)
    client_name: Optional[str] = None
    client_phone: Optional[str] = None
    trainer_id: int = Field(foreign_key="trainer.id_trainer")

    client: Optional[Client] = Relationship(back_populates="bookings")
    slot: Optional[Schedule] = Relationship(back_populates="booking")
    trainer: Optional[Trainer] = Relationship(back_populates="bookings")