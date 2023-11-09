
from sqlalchemy import create_engine
from models import Base, Audition, Role
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///theater.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()