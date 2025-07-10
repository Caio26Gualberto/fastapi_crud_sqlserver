from sqlalchemy import Column, Integer, String
from app.database import Base

class Person(Base):
    __tablename__ = "Pessoas"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)