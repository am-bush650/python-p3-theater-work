<<<<<<< HEAD
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
=======
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker


Base = declarative_base()#Base class for sqlalchemy models



class Role(Base):#represents roles in theater
    __tablename__ = 'roles'#table name in database

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)#name of character

    #One-to-Many relationship: A role can have multiple auditions
    auditions = relationship("Audition", back_populates="role")

    def actors(self):# Returns a list of actor names auditioning for this role
        return [audition.actor for audition in self.auditions]

    def locations(self):# Returns list of locations where auditions for the role took place
        return [audition.location for audition in self.auditions]

    def lead(self):# Returns the first hired actor for the role, or message if no one is hired
        hired_auditions = [a for a in self.auditions if a.hired]
        return hired_auditions[0] if hired_auditions else "no actor has been hired for this role"

    def understudy(self):# Returns the second hired actor for the role, or a message if no understudy is hired
        hired_auditions = [a for a in self.auditions if a.hired]# Filter hired auditions
        return hired_auditions[1] if len(hired_auditions) > 1 else "no actor has been hired for understudy for this role"
>>>>>>> 149185a (lib/alembic/)


class Audition(Base):
    __tablename__ = 'auditions'

<<<<<<< HEAD
    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    role = relationship('Role', backref=backref('auditions'))
    

=======
    id = Column(Integer, primary_key=True)# Primary key (unique identifier)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))# ForeignKey: Each audition is linked to one role


    # Many-to-One relationship: Each audition belongs to a single role
    role = relationship("Role", back_populates="auditions")

    
    # Method to update the hired status of an audition (actor gets the role)
>>>>>>> 149185a (lib/alembic/)
    def call_back(self):
        self.hired = True


<<<<<<< HEAD
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
=======
engine = create_engine('sqlite:///theater.db', echo=True)
Base.metadata.create_all(engine)

>>>>>>> 149185a (lib/alembic/)
Session = sessionmaker(bind=engine)
session = Session()