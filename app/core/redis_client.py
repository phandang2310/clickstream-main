import redis.asyncio as redis
from app.core.config import settings

# Khởi tạo pool kết nối Redis
redis_pool = redis.from_url(settings.redis_url, decode_responses=True)

async def get_redis():
    return redis_pool