from app.core.db import statistics_collection
from app.core.utils import CustomError
from app.crud.statistics import create_or_update_statistics
from app.schemas.statistics import StatisticsUpdate


class StatisticsService:
    @staticmethod
    async def add_or_edit_statistics(update_data: StatisticsUpdate):
        query_filter = {"user_id": update_data.user_id, "daily_stats.date": update_data.date}
        existing_stat = await statistics_collection.find_one(query_filter, {"daily_stats.$": 1})
        query_filter2 = {"user_id": update_data.user_id}
        category = "expense" if update_data.is_expense else "income"
        new_data = None

        if existing_stat:
            new_data = {
                "$set": {
                    "average_expense": update_data.average_expense,
                    "average_income": update_data.average_income
                },
                "$inc": {
                    f"daily_stats.$.{category}": update_data.amount if update_data.add else -update_data.amount
                }
            }
            return await create_or_update_statistics(statistics_collection, query_filter, new_data)
        elif update_data.add:
            new_data = {
                "$set": {
                    "average_income": update_data.average_income,
                    "average_expense": update_data.average_expense
                },
                "$push": {
                    "daily_stats": {
                        "date": update_data.date,
                        "income": update_data.amount if not update_data.is_expense else 0,
                        "expense": update_data.amount if update_data.is_expense else 0
                    }
                }
            }
            return await create_or_update_statistics(statistics_collection, query_filter2, new_data)
        if not new_data:
            raise CustomError(status_code=400, name="Нет транзакций для редактирования")

    @staticmethod
    async def get_statistics(user_id: int):
        result = await statistics_collection.find_one({"user_id": user_id})
        if not result:
            raise CustomError(status_code=400, name="У пользователя нет статистики")
        return result
