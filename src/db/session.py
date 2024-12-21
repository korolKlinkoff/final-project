from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from redis.asyncio import Redis

from core.config import settings

from db.repo.service.request_validation import ValidationRpcClient


engine = create_async_engine(
    settings.POSTGRES_DSN, echo=True
)

async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False,
    autocommit=False, autoflush=False
)

redis_connection = Redis(host=settings.REDIS_DB_HOST, port=settings.REDIS_DB_PORT)

validation_client = ValidationRpcClient()
