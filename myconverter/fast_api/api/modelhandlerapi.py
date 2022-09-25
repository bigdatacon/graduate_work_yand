from typing import List, Optional
from fastapi import APIRouter, Depends, Header
from services.modelhandlerservice import ModelHandler, get_modelhandler_service

router = APIRouter()


@router.get("/")
async def get_hw(
        modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    result = await modelhandler_service.get_model_object('http://127.0.0.1:8000/filmwork/')
    return result