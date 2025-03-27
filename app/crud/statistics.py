from motor.motor_asyncio import AsyncIOMotorCollection


async def create_or_update_statistics(collection: AsyncIOMotorCollection, query_filter: dict, new_data: dict):
    result = await collection.update_one(query_filter, new_data, upsert=True)
    return result
