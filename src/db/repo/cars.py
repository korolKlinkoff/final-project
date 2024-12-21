from sqlalchemy import select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession
from db.model import Cars


class CarsRepository:

    @staticmethod
    async def get_all(session: AsyncSession) -> ScalarResult[Cars]:
        query = select(Cars)  # SELECT * FROM cars;
        result = await session.execute(query)
        cars = result.scalars()

        return cars

    @staticmethod
    async def create(session: AsyncSession, **kwargs) -> None:
        obj = Cars(**kwargs)
        session.add(obj)
        await session.commit()
