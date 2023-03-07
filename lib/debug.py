
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base, PetItem, Store, ShoppingCart

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///pet_stores.db')
    Base.metadata.create_all(engine)
   
    Session = sessionmaker(bind=engine)
    session = Session()

    blah = PetItem(name = "bleh", quantity = 2, unit_price = 12.68)

    

    # Base.metadata.create_all(engine)
    import ipdb; ipdb.set_trace()

    
    