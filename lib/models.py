from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, MetaData
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


class Audition(Base):
    ___tablename___ = 'auditions'
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    Phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    def call_back(self):
        self.hired = True


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character_name = Column(String)


engine = create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()