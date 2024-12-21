from pydantic import BaseModel


class Driver(BaseModel):
    name: str
    phone_number: int
    car_number: str

    # def __init__(self, name, phone_number, car_number):
    #     self.name = name
    #     self.phone_number = phone_number
    #     self.car_number = car_number
