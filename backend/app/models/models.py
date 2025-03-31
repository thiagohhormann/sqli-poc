from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column("person_id", Integer, primary_key=True)
    name = Column(String, nullable=False)
    birthday = Column(Integer)
    password = Column(String)

    def __repr__(self):
        return f"{type(self).__name__}(id={self.id}, name={self.name})"
