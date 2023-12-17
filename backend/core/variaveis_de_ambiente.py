from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuracoes(BaseSettings):
    db_name:str = "projeto"
    db_user:str = "postgres"
    db_password:str = "postgres"
    db_port:str = 5432
    db_host:str = "db"
    
    uri:str = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    echo:bool = False

    model_config = SettingsConfigDict(extra="ignore", env_file=".env")

@lru_cache
def variaveis_ambiente()->Configuracoes:
    dados = Configuracoes
    return dados

