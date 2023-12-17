from fastapi import FastAPI, APIRouter
from backend.api.v1 import v1_routers

def register_routes(app: FastAPI):
    app.include_router(v1_routers)

def create_app() -> FastAPI:
    app = FastAPI (
        title="Templeta FastAPI",
        version="0.1.0",
        description="Template FastAPI Assíncrono com Postgres"
    )
    register_routes(app)
    return app



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(factory=True, app="backend.app:create_app", port=8001, host="0.0.0.0", reload=True)
