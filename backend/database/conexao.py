from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from backend.core.variabeis_de_ambiente import variaveis_ambiente

variaveis_ambiente = variaveis_ambiente()

# Configurações do banco de dados
db_uri = variaveis_ambiente.uri
db_echo = variaveis_ambiente.ech

# Configuração do create engine com os connect_args
async_engine = create_async_engine(url=db_uri, echo=db_echo, pool_pre_ping=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False, autocommit=False, autoflush=False)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

ActiveSession = Depends(get_session)
