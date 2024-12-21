from sqlalchemy.ext.asyncio import AsyncSession
from db.session import async_session
from db.repo import CarsRepository


async def get_all_cars():
    async with async_session() as session:  # type: AsyncSession
        cars = await CarsRepository.get_all(session)

    result = {}

    for car in cars:
        result[car.id] = {
            "mark": car.mark,
            "model": car.model,
            "color": car.color,
            "horsepower": car.horsepower,
            "number": car.number
        }

    return result
