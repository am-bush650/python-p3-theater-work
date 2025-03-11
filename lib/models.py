from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


class Audition(Base):
    ___tablename___ = 'auditions'
    actor = Column(String)
    location = Column(String)
    Phone = Column(Integer)
    hired = Column(Boolean)
    role_id = Column(Integer, primary_key=True)


class Role(Base):
    __tablename__ = 'roles'
    character_name = Column(String)



    """|| Column | Type |
| --- | --- |
| character_name | string |"""