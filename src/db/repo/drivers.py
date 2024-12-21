from db.session import redis_connection, validation_client
from schemas.drivers import Driver


class DriversRepository:
    @staticmethod
    async def create(driver: Driver):
        if not await validation_client.call(driver.phone_number):
            return False
        i = (await redis_connection.get("i"))
        if i is not None:
            i = i.decode()
            await redis_connection.set("i", int(i) + 1)
        else:
            await redis_connection.set("i", 1)
            i = 0
        await redis_connection.hset(i, "name", driver.name)
        await redis_connection.hset(i, "phone_number", driver.phone_number)
        await redis_connection.hset(i, "car_number", driver.car_number)
        return True

    @staticmethod
    async def get(driver_id) -> Driver:
        return Driver(name=await redis_connection.hget(driver_id, "name"),
                      phone_number=await redis_connection.hget(driver_id, "phone_number"),
                      car_number=await redis_connection.hget(driver_id, "car_number"))
