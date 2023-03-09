#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from rich import print

from db.models import Store, PetItem, pet_item_store
from helpers import (create_store_table, create_pet_item_table, YES, NO)

#  , fill_cart, show_cart, collect_payment

engine = create_engine('sqlite:///pet_stores.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print('''
    __________                 __    __ /\        __________        __          
    \______   \_______   _____/  |__/  |)/ ______ \______   \ _____/  |_  ______
    |    |  _/\_  __ \_/ __ \   __\   __\/  ___/  |     ___// __ \   __\/  ___/
    |    |   \ |  | \/\  ___/|  |  |  |  \___ \   |    |   \  ___/|  |  \___ \ 
    |______  / |__|    \___  >__|  |__| /____  >  |____|    \___  >__| /____  >
            \/              \/                \/                 \/          \/ 
                |\_/|        D\___/\
                (0_0)         (0_o)
               ==(Y)==         (V)
    ----------(u)---(u)----oOo--U--oOo---
    __|_______|_______|_______|_______|___''')
    print("Welcome to Brett's Pets!")
    print('Here is a list of available stores:')

    cart= []

    # Get a choice of store, retrieve an object from the DB
    while True:
        stores = session.query(Store)
        create_store_table(stores)
        store = None
        while not store:
            store_id = input('Which pet store would you like to shop at?  ')
            store = session.query(Store).filter(Store.id == store_id).one_or_none()

        print(f'Here is a list of pets at {store.name}:  ')
        pets = session.query(PetItem).filter(PetItem.stores.any(id=store.id))
        #.filter(PetItem.id = pet_item_store.pet_items_id).filter(PetItemsStore.store_id=store)
        create_pet_item_table(pets)

        pet = None
        while not pet:
            pet_id = input("Enter the ID of the pet you would like to adopt:")
            pet= session.query(PetItem).filter(PetItem.id == pet_id).one_or_none()

        print(f'You have selected {pet.name}. Their adoption fee ${pet.unit_price:.2f}.')
        cart.append(pet)
        #print(f'{cart}')

        answer = input("Would you like to adopt another pet? (y/n)").lower()
        if answer in NO:
            total_cost = sum(pet.unit_price for pet in cart)
            print(f'Your total adoption fee(s) is ${total_cost:.2f}. Thank you for shopping with Brett\'s Pets')
            break
        
        # Start adding items to cart
        # shopping_cart, cart_total = fill_cart(session, store)
        # print('Here are the items in your cart:')
        # show_cart(shopping_cart)

        # # Remove unwanted items from cart
        # remove_from_cart(session, shopping_cart, cart_total)

        # # Collect payment
        # print(f'Your total is ${cart_total:.2f}\n')
        # collect_payment(cart_total)

        # print('Thank you for using the Code Blooded pet store checkout CLI!\n')
