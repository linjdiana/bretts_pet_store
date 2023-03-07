from random import random, randint, choice as rc

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Store, PetItem, ShoppingCart, Order, pet_item_store

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

def create_pet_items():
    pet_items = [PetItem(
        name = fake.name(),
        quantity=randint(0, 10),
        unit_price = round(float(randint(0, 50)) + random(), 2)
    ) for i in range(50)]
    session.add_all(pet_items)
    session.commit()
    return pet_items

def create_shopping_carts():
    shoppingcarts = [ShoppingCart() for i in range(50)]
    session.add_all(shoppingcarts)
    session.commit()
    return shoppingcarts

def create_orders():
    print("Deleting existing order...")
    session.query(Order).delete()
    session.commit()

    print("Creating an order...")
    orders = [Order() for i in range(10)]
    session.add_all(orders)
    session.commit()

    return orders


if __name__ == '__main__':
    
    session.query(pet_item_store).delete()
    session.commit()

    pet_items = create_pet_items()
    stores = create_stores()
    shoppingcarts = create_shopping_carts(pet_items, stores)
    orders = create_orders()