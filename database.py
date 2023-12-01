# database.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)
metadata = declarative_base()

class IoT(metadata):
    __tablename__ = "iot"
    id = Column(Integer, primary_key=True, index=True)
    dispositivo = Column(String, index=True)
    valor = Column(Integer)

engine = create_engine(DATABASE_URL)
metadata.create_all(bind=engine)
