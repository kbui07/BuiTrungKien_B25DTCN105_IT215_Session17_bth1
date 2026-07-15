from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class WarehouseModel(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True)
    warehouse_name = Column(String(100), nullable=False)
    location = Column(String(200), nullable=False)

    packages = relationship("PackageModel", back_populates="warehouse")