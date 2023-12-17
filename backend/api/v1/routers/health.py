from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

endpoints = APIRouter()

@endpoints.get("")
async def _health_check():
    return JSONResponse({"status": "ok"}, status_code=status.HTTP_200_OK)