from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from .association import package_truck

class TruckModel(Base):
    __tablename__ = "trucks"

    id = Column(Integer, primary_key=True)
    license_plate = Column(String(20), nullable=False)

    packages = relationship(
        "PackageModel",
        secondary=package_truck,
        back_populates="trucks"
    )