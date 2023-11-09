from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__ = 'auditions'
    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(String())
    role_id = Column(Integer(), ForeignKey('roles.id'))

    def __repr__(self):
        return f'Audition({self.actor}, {self.location}, {self.hired})'
        
    

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())

    auditions = relationship('Audition', backref='role')

    def __repr__(self):
        return f'Role({self.character_name})'