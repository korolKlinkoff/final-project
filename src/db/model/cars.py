from sqlalchemy import Column, Integer, String
from db.model.base import Base


class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, autoincrement=True)
    mark = Column(String, nullable=False)
    model = Column(String, nullable=False)
    color = Column(String, nullable=False)
    horsepower = Column(Integer, nullable=True)
    number = Column(String, nullable=True, unique=True)
