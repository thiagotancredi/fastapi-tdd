from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

endpoints = APIRouter()

@endpoints.get("")
async def teste_usuario():
    return JSONResponse({"status": "teste_usuario"}, status_code=status.HTTP_200_OK)