from fastapi import FastAPI, Depends
from app.server.auth.jwt_bearer import JWTBearer
from app.server.routes.scan import router as ScanRouter
from app.server.routes.user import router as UserRouter

app = FastAPI()

token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Sangkuriang."}


app.include_router(UserRouter, tags=["[TESTING PURPOSE] - Users"], prefix="/user")
app.include_router(ScanRouter, tags=["Scans"], prefix="/scan", dependencies=[Depends(token_listener)])

