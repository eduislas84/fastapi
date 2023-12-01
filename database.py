from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class IoT(Base):
    __tablename__ = "iot"

    id = Column(Integer, primary_key=True, index=True)
    dispositivo = Column(String, index=True)
    valor = Column(Integer)

Base.metadata.create_all(bind=engine)
