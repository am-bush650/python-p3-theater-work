<<<<<<< HEAD
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker, declarative_base
=======
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import os
>>>>>>> 57187fe (alembic.ini)

Base = declarative_base()

<<<<<<< HEAD
Base = declarative_base(metadata=metadata)


class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    role = relationship('Role', backref=backref('auditions'))
    

    def call_back(self):
        self.hired = True


    def __repr__(self):
        return f"<Audition(id={self.id}, actor='{self.actor}', hired={self.hired})>"


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    auditions = relationship('Audition', back_populates='role', cascade="all, delete-orphan")

    def lead(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[0] if hired_auditions else "no actor has been hired for this role"

    @property
    def actors(self):
        return[audition.actor for audition in self.auditions]
    
    @property
    def locations(self):
        return[audition.location for audition in self.auditions]
    
    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else "no actor has been hired for understudy for this role"
 

    def __repr__(self):
        return f"<Role(id={self.id}, character_name='{self.character_name}')>"
    

engine = create_engine('sqlite:///theater.db', echo=True)
Base.metadata.create_all(engine)

=======
class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean(), default=False)
    role_id = Column(Integer(), ForeignKey('roles.id'))

    role = relationship('Role', back_populates='auditions')

    def call_back(self):  # Marks an audition as hired
        self.hired = True

    def __repr__(self):
        return f"<Audition(id={self.id}, actor='{self.actor}', hired={self.hired})>"

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())

    auditions = relationship('Audition', back_populates='role')

    @property
    def actors(self):
        return [audition.actor for audition in self.auditions]

    @property
    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if not hired_auditions:
            return 'no actor has been hired for this role'
        return hired_auditions[0]

    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if len(hired_auditions) < 2:
            return 'no actor has been hired for understudy for this role'
        return hired_auditions[1]

    def __repr__(self):
        return f"<Role(id={self.id}, character_name='{self.character_name}')>"



engine = create_engine("sqlite:///theatre.db", echo=True)
Base.metadata.create_all(engine)


>>>>>>> 57187fe (alembic.ini)
Session = sessionmaker(bind=engine)
session = Session()