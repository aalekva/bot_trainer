from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:Larryisreal@localhost:5432/bot_trainer"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)  # возвращает объект Session для использования в with

def create_db_and_tables():
    from models import Client, Trainer, Schedule, Booking
    SQLModel.metadata.create_all(engine)
