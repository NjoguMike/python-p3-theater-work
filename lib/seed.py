from models import Base, Audition, Role
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random

if __name__ == '__main__':
    engine = create_engine('sqlite:///theater.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()

    session.query(Role).delete()
    positions = ['co-lead', 'driver', 'fiction',
        'lead-actor', 'cre-member', 'writer']
    roles = []
    for i in range(10):
        role = Role(
            character_name = random.choice(positions)
        )

        
        session.add(role)
        session.commit()
        roles.append(role)
    
    # session.query(Audition).delete()
    auditions = []
    for role in roles:
        audition = Audition(
            actor = fake.name(),
            location = fake.unique.address(),
            phone = fake.phone_number(),
            hired = 0,
            role_id = role.id
        )

        
        session.add(audition)
        session.commit()
        auditions.append(audition)
