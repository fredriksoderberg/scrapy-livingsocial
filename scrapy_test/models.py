from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.engine.url import URL

DeclarativeBase = declarative_base()

def create_deals_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class Deals(DeclarativeBase):
    __tablename__ = "deals"
    
    id = Column(Integer, primary_key = True)
    title = Column('title', String)
    link = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    original_price = Column('original_price', String, nullable=True)
    price = Column('price', String, nullable=True)
    end_date = Column('end_date', DateTime, nullable=True)
    
    
    
