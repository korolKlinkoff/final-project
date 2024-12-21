from fastapi import APIRouter
from schemas.drivers import Driver
from db.repo.drivers import DriversRepository


router = APIRouter()


@router.get("")
async def root():
    return {"message": "Hi"}


@router.get("/get/{driver_id}")
async def get_driver(driver_id):
    return await DriversRepository.get(driver_id)


@router.post("/create")
async def create_driver(driver: Driver):
    return await DriversRepository.create(driver)
