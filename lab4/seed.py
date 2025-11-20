from datetime import datetime, timedelta
from sqlmodel import Session, create_engine
from models import Client, Trainer, Schedule, Booking

# Подключение к базе
DATABASE_URL = "postgresql+psycopg2://postgres:Larryisreal@localhost:5432/bot_trainer"
engine = create_engine(DATABASE_URL, echo=True)

# ================================
# 1. Создаём минимальный набор данных
# ================================
def seed_data():
    with Session(engine) as session:

        # ----- Клиенты -----
        client1 = Client(id_client=123456, full_name="Иван Иванов", phone="+79991234567", username="ivan")
        client2 = Client(id_client=234567, full_name="Мария Петрова", phone="+79997654321", username="maria")
        session.add_all([client1, client2])

        # ----- Тренеры -----
        trainer1 = Trainer(full_name="Алексей Смирнов", qualification="Сертификат тренера", specialization="Йога")
        trainer2 = Trainer(full_name="Екатерина Кузнецова", qualification="Сертификат фитнес", specialization="Пилатес")
        session.add_all([trainer1, trainer2])
        session.commit()  # commit, чтобы появились id тренеров

        # ----- Расписание (слоты) -----
        now = datetime.now()
        slot1 = Schedule(trainer_id=trainer1.id_trainer, slot_timestamp=now + timedelta(days=1))
        slot2 = Schedule(trainer_id=trainer1.id_trainer, slot_timestamp=now + timedelta(days=2))
        slot3 = Schedule(trainer_id=trainer2.id_trainer, slot_timestamp=now + timedelta(days=1))
        slot4 = Schedule(trainer_id=trainer2.id_trainer, slot_timestamp=now + timedelta(days=3))
        session.add_all([slot1, slot2, slot3, slot4])
        session.commit()  # commit, чтобы появились id слотов

        # ----- Записи (бронирования) -----
        booking1 = Booking(client_id=client1.id_client, slot_id=slot1.id_slot,
                           client_name=client1.full_name, client_phone=client1.phone)
        booking2 = Booking(client_id=client2.id_client, slot_id=slot3.id_slot,
                           client_name=client2.full_name, client_phone=client2.phone)
        session.add_all([booking1, booking2])

        session.commit()
        print("База данных успешно заполнена тестовыми данными!")

# Запуск
if __name__ == "__main__":
    seed_data()
