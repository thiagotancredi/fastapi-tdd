from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

endpoints = APIRouter()

@endpoints.get("")
async def teste_categoria():
    return JSONResponse({"status": "teste_categoria"}, status_code=status.HTTP_200_OK)