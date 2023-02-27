from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .index import Base

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    description = Column(String(100), nullable=False)
    owner_id = Column(Integer, ForeignKey("employee.id", ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    owner = relationship("Employee", back_populates="products")
    
    