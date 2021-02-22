from fastapi import FastAPI, Depends


from app.auth.jwt_bearer import JWTBearer
from app.routes.scan import router as ScanRouter
from app.routes.admin import router as AdminRouter

app = FastAPI()

token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Sangkuriang."}

# Extended router
app.include_router(ScanRouter, tags=["Scans"], prefix="/scan", dependencies=[Depends(token_listener)])
app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
