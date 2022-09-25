from typing import List, Optional
from fastapi import APIRouter, Depends, Header
from services.apit import ApiTesting, get_apitesting_service

router = APIRouter()


@router.get("/")
async def get_hw(
        apitest_service: ApiTesting = Depends(get_apitesting_service),
):
    dashboards = await apitest_service.get_list()
    return dashboards