from random import random, randint, choice as rc

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Store, PetItem, ShoppingCart, pet_item_store

engine = create_engine('sqlite:///pet_stores.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def create_stores():
    stores = [Store(
        name=fake.name() + "'s Pet Shop",
        address=fake.address(),
    ) for i in range(10)]
    session.add_all(stores)
    session.commit()
    return stores

def create_petitems():
    petitems = [PetItem(
        name = fake.name(),
        quantity=randint(0, 10),
        unit_price = round(float(randint(0, 50)) + random(), 2)
    ) for i in range(50)]
    session.add_all(petitems)
    session.commit()
    return petitems

def create_shoppingcarts():
    shoppingcarts = [ShoppingCart() for i in range(50)]
    session.add_all(shoppingcarts)
    session.commit()
    return shoppingcarts

if __name__ == '__main__':
    games = create_stores()
    reviews = create_petitems()
    users = create_shoppingcarts()

