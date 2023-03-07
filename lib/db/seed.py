from random import random, randint, choice as rc

# from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import PetItem, ShoppingCart, Store, pet_item_store

engine = create_engine('sqlite:///grocery_stores.db')
Session = sessionmaker(bind=engine)
session = Session()