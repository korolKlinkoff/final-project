from fastapi import APIRouter
from api.v1.cars import router as car_router
from api.v1.drivers import router as driver_router


api_router = APIRouter()

api_router.include_router(car_router, prefix="/cars")
api_router.include_router(driver_router, prefix="/drivers")

