from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from datetime import datetime
from requests import get_trainer_schedule, create_slot, update_slot, delete_slot

router = APIRouter(prefix="/schedule", tags=["Schedule"])

class SlotSchema(BaseModel):
    id_slot: int
    trainer_id: int
    slot_timestamp: datetime
    status: str

    model_config = {"from_attributes": True}  # Pydantic V2

class SlotCreateSchema(BaseModel):
    slot_timestamp: datetime

class SlotUpdateSchema(BaseModel):
    slot_timestamp: datetime | None = None
    status: str | None = None

@router.get(
    "/trainer/{trainer_id}",
    response_model=List[SlotSchema],
    summary="Слоты тренера",
    description="Возвращает список всех слотов выбранного тренера. По умолчанию выводятся только свободные слоты."
)
def api_get_trainer_free_slots(trainer_id: int):
    slots = get_trainer_schedule(trainer_id)
    return slots


@router.post(
    "/trainer/{trainer_id}",
    response_model=SlotSchema,
    summary="Создать слот",
    description="Создаёт новый свободный слот для тренера на указанное время."
)
def api_create_slot(trainer_id: int, data: SlotCreateSchema):
    return create_slot(trainer_id, data.slot_timestamp)


@router.put(
    "/{slot_id}",
    response_model=SlotSchema,
    summary="Редактировать слот",
    description=(
        "Обновляет данные слота: дату/время или статус. "
        "Если слот уже занят, изменить его на 'free' нельзя."
    )
)
def api_update_slot(slot_id: int, data: SlotUpdateSchema):
    slot = update_slot(slot_id, data.slot_timestamp, data.status)
    if not slot:
        raise HTTPException(status_code=400, detail="Невозможно обновить слот")
    return slot


@router.delete(
    "/{slot_id}",
    summary="Удалить слот",
    description="Удаляет слот, если он свободен. Занятые слоты удалить нельзя."
)
def api_delete_slot(slot_id: int):
    if not delete_slot(slot_id):
        raise HTTPException(status_code=400, detail="Невозможно удалить слот")
    return {"status": "ok", "message": "Слот удалён"}
