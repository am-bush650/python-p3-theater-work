from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# Base class for SQLAlchemy models
Base = declarative_base()


# Define the Role model represents roles in the theater
class Role(Base):
    __tablename__ = 'roles'# Table name in the database

    id = Column(Integer, primary_key=True)# Primary key (unique identifier)
    character_name = Column(String, nullable=False)

    
    # One-to-Many relationship: A role can have multiple auditions
    auditions = relationship("Audition", back_populates="role")
    
    # Returns a list of actor names auditioning for this role
    def actors(self):
        return [audition.actor for audition in self.auditions]
    
    # Returns a list of locations where auditions for this role took place
    def locations(self):
        return [audition.location for audition in self.auditions]
    
    # Returns the first hired actor for the role, or a message if no one is hired
    def lead(self):
        hired_auditions = [a for a in self.auditions if a.hired]
        return hired_auditions[0] if hired_auditions else "no actor has been hired for this role"
    
    # Returns the first hired actor for the role, or a message if no one is hired
    def understudy(self):
        hired_auditions = [a for a in self.auditions if a.hired]# Filter hired auditions
        return hired_auditions[1] if len(hired_auditions) > 1 else "no actor has been hired for understudy for this role"

# Define the Audition model represents actors auditioning for roles
class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)# Primary key (unique identifier)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id')) # ForeignKey: Each audition is linked to one role


    # Many-to-One relationship: Each audition belongs to a single role
    role = relationship("Role", back_populates="auditions")


    # Method to update the hired status of an audition
    def call_back(self):
        self.hired = True


engine = create_engine('sqlite:///theater.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
