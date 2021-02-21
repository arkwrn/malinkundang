from fastapi import FastAPI
from app.server.routes.scan import router as ScanRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Sangkuriang."}

app.include_router(ScanRouter, tags=["Scans"], prefix="/scan")

