from fastapi import APIRouter, HTTPException
from typing import List
from models import Client
from requests import get_all_clients, get_client_by_id

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.get(
    "/",
    response_model=List[Client],
    summary="Список всех клиентов",
    description="Возвращает список всех клиентов с их именами, телефонами, username и датой создания."
)
def api_get_clients():
    return get_all_clients()


@router.get(
    "/{client_id}",
    response_model=Client,
    summary="Данные конкретного клиента",
    description="Возвращает данные клиента по его ID. Если клиент не найден, возвращает ошибку 404."
)
def api_get_client(client_id: int):
    client = get_client_by_id(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

