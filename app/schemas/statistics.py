from typing import List

from pydantic import BaseModel
from datetime import date


class StatisticsUpdate(BaseModel):
    user_id: int
    average_income: float
    average_expense: float
    date: str
    amount: float
    add: bool
    is_expense: bool


class DailyStatsSchema(BaseModel):
    date: date
    income: float
    expense: float


class StatisticsResponse(BaseModel):
    average_income: float
    average_expense: float
    daily_stats: List[DailyStatsSchema]
