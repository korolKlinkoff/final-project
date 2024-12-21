from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from api.service.cars import get_all_cars

from db.repo import CarsRepository
from db.session import async_session

from schemas import Car

router = APIRouter()


@router.get("")
async def root():
    return {"message": "Hi"}


@router.get('/list')
async def list_cars():
    return await get_all_cars()


@router.post('/create')
async def create_car(item: Car):
    async with async_session() as session:  # type: AsyncSession
        await CarsRepository.create(session, **item.model_dump())
