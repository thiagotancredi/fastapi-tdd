from fastapi import APIRouter

from .routers.health import endpoints as health_endpoints
from .routers.categoria import endpoints as categoria_endpoints
from .routers.produto import endpoints as produto_endpoints
from .routers.usuario import endpoints as usuario_endpoints


v1_routers = APIRouter()

v1_routers.include_router(health_endpoints, prefix="/health", tags=["health"])
v1_routers.include_router(categoria_endpoints, prefix="/categorias", tags=["categoria"])
v1_routers.include_router(produto_endpoints, prefix="/produtos", tags=["produto"])
v1_routers.include_router(usuario_endpoints, prefix="/usuarios", tags=["usuario"])