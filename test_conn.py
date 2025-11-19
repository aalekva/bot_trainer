import psycopg2

try:
    conn = psycopg2.connect(
        dbname="bot_trainer",
        user="postgres",
        password="Larryisreal",
        host="localhost",
        port="5432"
    )
    print("Соединение прошло успешно!")
except Exception as e:
    print("Ошибка соединения:", e)
