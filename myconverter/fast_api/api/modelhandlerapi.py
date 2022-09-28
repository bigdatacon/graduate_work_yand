from typing import List, Optional
from fastapi import APIRouter, Depends, Header
from services.modelhandlerservice import ModelHandler, get_modelhandler_service

router = APIRouter()


@router.get("/")
async def get_model_object(
        modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    result = await modelhandler_service.get_model_object()
    return result


@router.get("/get_model_object_by_id")
async def get_model_object_by_id(film_uuid,
        modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    result = await modelhandler_service.get_model_object_by_id(film_uuid)
    return result


@router.get("/resize")
async def resize(input_file_path,
        modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    result = await modelhandler_service.resize(input_file_path)
    return result