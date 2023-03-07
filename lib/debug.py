
# from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import PetItem, Store, ShoppingCart

# fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///pet_stores.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    import ipdb; ipdb.set_trace()