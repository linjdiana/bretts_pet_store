#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rich.console import Console

from db.models import Store, PetItem, pet_item_store
from helpers import (create_store_table, create_pet_item_table, YES, NO)

console = Console()

#  , fill_cart, show_cart, collect_payment

engine = create_engine('sqlite:///pet_stores.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    console.print('''[dark_cyan]
    __________                 __    __ /\        __________        __          
    \______   \_______   _____/  |__/  |)/ ______ \______   \ _____/  |_  ______
    |    |  _/\_  __ \_/ __ \   __\   __\/  ___/  |     ___// __ \   __\/  ___/
    |    |   \ |  | \/\  ___/|  |  |  |  \___ \   |    |   \  ___/|  |  \___ \ 
    |______  / |__|    \___  >__|  |__| /____  >  |____|    \___  >__| /____  >
            \/              \/                \/                 \/          \/ 
            
                            |\_/|        D\___/\\
                            (0_0)         (0_o)
                           ==(Y)==         (V)
                ----------(u)---(u)----oOo--U--oOo---
                __|_______|_______|_______|_______|___''')
    console.print("[bold yellow]Welcome to Brett\'s Pets! ""\U0001F63B""\U0001F429""\U0001F9A7")
    console.print('[bold dark_orange]Here is a list of available stores:')

    cart= []

    # Get a choice of store, retrieve an object from the DB
    while True:
        stores = session.query(Store)
        create_store_table(stores)
        store = None
        while not store:
            store_id = console.input('[bold yellow]Which pet store would you like to shop at?  ')
            store = session.query(Store).filter(Store.id == store_id).one_or_none()

        console.print(f'[bold red]Here is a list of pets at {store.name}:  ')
        pets = session.query(PetItem).filter(PetItem.stores.any(id=store.id))
        create_pet_item_table(pets)

        pet = None
        while not pet:
            pet_id = console.input("[bold yellow]Enter the ID of the pet you would like to adopt:")
            pet= session.query(PetItem).filter(PetItem.id == pet_id).one_or_none()

        console.print(f'[bold magenta]You have selected {pet.name}. Their adoption fee ${pet.unit_price:.2f}.')
        cart.append(pet)

        answer = console.input("[bold dark_turquoise]Would you like to adopt another pet? (y/n)").lower()
        if answer in NO:
            total_cost = sum(pet.unit_price for pet in cart)

            console.print(f'[bold dark_red]Your total adoption fee(s) is ${total_cost:.2f}.')
            console.print('''[blue]
                 ___ _,_  _, _, _ _,_   , _  _, _,_   __,  _, __,    _, _,_  _, __, __, _ _, _  _,   _  _ _ ___ _,_   __, __, __, ___ ___ ,  _,   __, __, ___  _, ,
                  |  |_| /_\ |\ | |_/   \ | / \ | |   |_  / \ |_)   (_  |_| / \ |_) |_) | |\ | / _   |  | |  |  |_|   |_) |_) |_   |   |  ' (_    |_) |_   |  (_  |
                  |  | | | | | \| | \    \| \_/ | |   |   \_/ | \   ,_) | | \ / |   |   | | \| \_/   |/\| |  |  | |   |_) | \ |_   |   |    ,_)   |   |_   |  ,_) |
                  ~  ~ ~ ~ ~ ~  ~ ~ ~     )  ~  `~'   ~    ~  ~ ~    ~  ~ ~  ~  ~   ~   ~ ~  ~  ~    ~  ~ ~  ~  ~ ~   ~   ~ ~ ~~~  ~   ~     ~    ~   ~~~  ~   ~  .
                                         ~'                                                                                                                        
                                                                   [light_sea_green] |\_/|                  
                                                                    | @ @   Woof! 
                                                                    |   <>              _             |\      _,,,---,,_ 
                                                                    |  _/\------____ ((| |))    ZZZzz /,`.-'`'    -.  ;-;;,_
                                                                    |               `--' |           |,4-  ) )-,_. ,\ (  `'-'
                                                                ____|_       ___|   |___.'          '---''(_/--'  `-'\_) 
                                                                /_/_____/____/_______|
            
            ''')
            break
       
