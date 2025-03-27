from fastapi import APIRouter, Depends

from app.core.security import get_current_user
from app.schemas.statistics import StatisticsUpdate, StatisticsResponse
from app.services.statistics import StatisticsService

router = APIRouter(prefix="/statistics")


@router.post("", response_model=dict)
async def add_or_edit_statistics(
        update_data: StatisticsUpdate,
):
    await StatisticsService.add_or_edit_statistics(update_data)
    return {"status": "ok"}


@router.get("", response_model=StatisticsResponse)
async def get_statistics(user_id: str = Depends(get_current_user)):
    return await StatisticsService.get_statistics(int(user_id))
