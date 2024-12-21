from pydantic import BaseModel


class Car(BaseModel):
    mark: str
    model: str
    color: str
    horsepower: int
    number: str
