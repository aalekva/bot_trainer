from sqlmodel import create_engine, SQLModel
from models import Client, Trainer, Schedule, Booking
from database import create_db_and_tables
from requests import get_all_clients, get_trainer_schedule

DATABASE_URL = "postgresql+psycopg2://postgres:Larryisreal@localhost:5432/bot_trainer"

engine = create_engine(DATABASE_URL, echo=True)

# Создаём все таблицы в базе
SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    # Создать таблицы (если ещё нет)
    create_db_and_tables()

    # Пример:все клиенты
    clients = get_all_clients()
    for client in clients:
        print(client.id_client, client.full_name, client.phone)

    # Пример:расписание тренера
    schedule = get_trainer_schedule(trainer_id=1)
    for slot in schedule:
        print(slot.id_slot, slot.slot_timestamp, slot.status)
