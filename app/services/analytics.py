import json
import time
from app.core.redis_client import redis_pool

class AnalyticsService:
    @staticmethod
    async def save_event(event_data: dict):
        # Tạo ID duy nhất bằng timestamp + random
        event_id = f"event:{int(time.time() * 1000)}"
        
        # 1. Lưu chi tiết event vào Hash
        await redis_pool.hset(event_id, mapping=event_data)
        
        # 2. Thêm vào danh sách theo dõi để thống kê (Sorted Set)
        # Dùng timestamp làm score để dễ dàng lọc theo thời gian
        await redis_pool.zadd("events_timeline", {event_id: time.time()})
        
        # 3. Tăng bộ đếm theo loại event (ví dụ: click, view)
        await redis_pool.hincrby("stats:event_types", event_data['event_type'], 1)
        
        return event_id

    @staticmethod
    async def get_stats():
        # Lấy bảng thống kê tổng hợp từ Redis
        return await redis_pool.hgetall("stats:event_types")