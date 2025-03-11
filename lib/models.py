from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker, declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


class Audition(Base):
    __tablename__ = 'auditions'
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    Phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    def call_back(self):
        self.hired = True

    role = relationship('Role', backref=backref('auditions'))


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character_name = Column(String)

    def lead(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[0] if hired_auditions else 'no actor has been hired for this role'

    @property
    def actors(self):
        return[audition.actor for audition in self.auditions]
    
    @property
    def locations(self):
        return [audition.location for audition in self.auditions]
    
    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else 'no actor has been hired for understudy for this role'
 



engine = create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()