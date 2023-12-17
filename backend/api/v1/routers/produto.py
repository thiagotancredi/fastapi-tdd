from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

endpoints = APIRouter()

@endpoints.get("")
async def teste_produto():
    return JSONResponse({"status": "teste_produto"}, status_code=status.HTTP_200_OK)