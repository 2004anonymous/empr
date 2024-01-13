from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .config import Base, engine

class UserTable(Base):

    __tablename__ = "User"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(60), nullable=False)

Base.metadata.create_all(engine)
