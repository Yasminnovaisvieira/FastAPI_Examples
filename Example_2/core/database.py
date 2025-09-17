from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import Settings

engire: AsyncEngine = create_async_engine(Settings.DB_URL)

Session: AsyncEngine = sessionmaker(
    # Para que não faça alterações no banco automaticamente
    autocommit = False
    autoflush= False
    # Evita que a conexão seja encerrada ao acontecer um commit
    expire_on_commit= False
    class_= AsyncSession
    bind= engire
)