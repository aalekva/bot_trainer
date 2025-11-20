from fastapi import APIRouter, HTTPException
from typing import List
from models import Trainer, Schedule
from requests import get_all_trainers, get_trainer_schedule

router = APIRouter(prefix="/trainers", tags=["Trainers"])

@router.get(
    "/",
    response_model=List[Trainer],
    summary="Список всех тренеров",
    description="Возвращает список всех тренеров с их полными данными: имя, специализация, контакты и описание"
)
def api_get_trainers():
    return get_all_trainers()


@router.get(
    "/{trainer_id}/schedule",
    response_model=List[Schedule],
    summary="Расписание тренера",
    description=(
        "Возвращает список слотов выбранного тренера. "
        "Параметр only_free=True (по умолчанию) возвращает только свободные слоты, "
        "если указать False — возвращаются все слоты."
    )
)
def api_get_schedule(trainer_id: int, only_free: bool = True):
    return get_trainer_schedule(trainer_id, only_free)