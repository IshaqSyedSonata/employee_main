from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .index import Base

class Employee(Base):
    __tablename__ = "employee"
    # __table_args__ = {'extend_existing': True}
    # __table_args__ = {'schema': 'schema_any'}
    # __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    address = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    products = relationship("Products", back_populates="owner")
    
    