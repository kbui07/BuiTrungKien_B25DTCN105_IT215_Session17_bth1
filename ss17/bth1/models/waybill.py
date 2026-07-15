from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class WaybillModel(Base):
    __tablename__ = "waybills"

    id = Column(Integer, primary_key=True)
    tracking_number = Column(String(100), nullable=False)
    shipping_status = Column(String(50), nullable=False)

    package_id = Column(Integer,ForeignKey("packages.id"),unique=True)

    package = relationship(
        "PackageModel",
        back_populates="waybill"
    )