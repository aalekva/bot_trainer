from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from requests import create_booking, get_bookings_by_trainer, get_bookings_by_client, cancel_booking, move_booking

router = APIRouter(prefix="/bookings", tags=["Bookings"])

# ===== Pydantic-схемы =====
class BookingCreateSchema(BaseModel):
    client_name: str
    client_phone: str
    trainer_id: int
    slot_id: int

class BookingMoveSchema(BaseModel):
    new_slot_id: int

class BookingSchema(BaseModel):
    id_booking: int
    client_name: Optional[str]
    client_phone: Optional[str]
    slot_id: int
    trainer_id: int
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}  # Pydantic V2
# =========================

@router.post(
    "/",
    response_model=BookingSchema,
    summary="Создать запись",
    description="Клиент записывается на выбранный слот. Требуются имя, телефон, ID тренера и ID слота. Если слот недоступен, возвращается ошибка 400."
)
def api_create_booking(data: BookingCreateSchema):
    booking = create_booking(data)
    if not booking:
        raise HTTPException(status_code=400, detail="Слот недоступен")
    return booking


@router.get(
    "/trainer/{trainer_id}",
    response_model=List[BookingSchema],
    summary="Записи тренера",
    description="Возвращает список всех записей на занятия выбранного тренера."
)
def api_get_trainer_bookings(trainer_id: int):
    return get_bookings_by_trainer(trainer_id)


@router.get(
    "/client/{client_id}",
    response_model=List[BookingSchema],
    summary="Записи клиента",
    description="Возвращает список всех записей конкретного клиента."
)
def api_get_client_bookings(client_id: int):
    return get_bookings_by_client(client_id)


@router.delete(
    "/{booking_id}",
    summary="Отменить запись",
    description="Отменяет запись по ID. Если запись невозможно отменить (например, уже завершена), возвращает ошибку 400."
)
def api_cancel_booking(booking_id: int):
    if not cancel_booking(booking_id):
        raise HTTPException(status_code=400, detail="Невозможно отменить запись")
    return {"status": "ok", "message": "Запись отменена"}


@router.put(
    "/{booking_id}",
    response_model=BookingSchema,
    summary="Перенести запись",
    description="Переносит запись клиента на другой слот. Требуется указать новый slot_id. Если перенос невозможен, возвращается ошибка 400."
)
def api_move_booking(booking_id: int, data: BookingMoveSchema):
    booking = move_booking(booking_id, data.new_slot_id)
    if not booking:
        raise HTTPException(status_code=400, detail="Невозможно перенести запись")
    return booking
