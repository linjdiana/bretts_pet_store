#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from rich import print

from db.models import Store
from helpers import (create_store_table, create_pet_item_table)

#  , fill_cart, show_cart, collect_payment

engine = create_engine('sqlite:///pet_stores.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print("Welcome to Brett's Pets!")
    print('Here is a list of available stores:')
    stores = session.query(Store)
    create_store_table(stores)

    # Get a choice of store, retrieve an object from the DB
    store = None
    while not store:
        store_id = input('Which pet store would you like to shop at?  ')
        store = session.query(Store).filter(Store.id == store_id).one_or_none()

    print('Here is a list of pets and pet items we sell:  ')
    create_pet_item_table(pet_items)

    # Start adding items to cart
    shopping_cart, cart_total = fill_cart(session, store)
    # print('Here are the items in your cart:')
    # show_cart(shopping_cart)

    # # Remove unwanted items from cart
    # remove_from_cart(session, shopping_cart, cart_total)

    # # Collect payment
    # print(f'Your total is ${cart_total:.2f}\n')
    # collect_payment(cart_total)

    # print('Thank you for using the Code Blooded pet store checkout CLI!\n')
