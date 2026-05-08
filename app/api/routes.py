from fastapi import APIRouter, Depends
from app.services.analytics import AnalyticsService

router = APIRouter()

@router.post("/track")
async def track_event(data: dict):
    event_id = await AnalyticsService.save_event(data)
    return {"status": "success", "event_id": event_id}

@router.get("/analytics")
async def get_analytics():
    stats = await AnalyticsService.get_stats()
    return stats