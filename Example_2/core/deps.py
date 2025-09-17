# Serve para conectar a sessão com o banco de dados

from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

# Injeção de dependências
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()