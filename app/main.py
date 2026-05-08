import redis
import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
app = FastAPI(title="Clickstream Analytics")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def home():
    return FileResponse(Path("app/static/index.html")  )

@app.post("/track")
async def track(request: Request):
    data = await request.json()
    r.lpush('clickstream', json.dumps(data))
    r.ltrim('clickstream', 0, 19)
    return {"status": "tracked", "message": "Saved to Redis"}

@app.get("/analytics")
def analytics():
    data = r.lrange('clickstream', 0, -1)
    events_from_redis = [json.loads(item) for item in data]
    return {"events": events_from_redis}