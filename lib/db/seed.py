from random import random, randint, choice as rc

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Store, PetItem, ShoppingCart, Order, pet_item_store

engine = create_engine('sqlite:///pet_stores.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

pet_stores = ["Purrfectly Pawsome", "The Furry Bunch", "The Bark Side", "Fur-Ever Friends", "Furry Fiesta", "Paws 'N Claws", "Critter Caboodle", "Bark 'N Purr ", "Wet Noses", "Wagging and Clawing"]

pet_names = ["Max", "Buddy", "Charlie", "Rocky", "Cooper", "Bear", "Duke", "Teddy", "Harley", "Oliver", "Jack", "Tucker", "Zeus", "Jake", "Winston", "Oscar", "Bailey", "Gus", "Loki", "Roxy", "Stella", "Maggie", "Luna", "Daisy", "Rosie", "Sadie", "Lucy", "Coco", "Chloe", "Lilly", "Sophie", "Zoe", "Abby", "Gracie", "Ruby", "Molly", "Emma", "Mia", "Ava", "Isabella", "Leah", "Avery", "Ella", "Scarlett", "Lila", "Nora", "Hazel", "Lucy", "Lily"]

pets = ["Domestic Long Hair", "Domestic Short Hair", "Siamese", "Ragdoll", "Persian", "Bengal", "Russian Blue", "Sphynx", "American Shorthair", "Scottish Fold", "Maine Coon", "Devon Rex", "Burmese", "Abyssinian", "Cornish Rex", "Himalayan", "Turkish Angora", "Tonkinese", "British Shorthair", "Oriental Shorthair", "Exotic Shorthair", "Chartreux", "Birman", "Norwegian Forest Cat", "Balinese", "Snowshoe", "Manx", "Somali", "Turkish Van", "Bombay", "Japanese Bobtail", "Singapura", "American Wirehair", "Egyptian Mau", "LaPerm", "Peterbald", "Selkirk Rex", "Ocicat", "Pixie-Bob", "Siberian Husky", "Labrador Retriever", "Golden Retriever", "Chihuahua", "Poodle", "Bulldog", "German Shepherd", "Boxer", "Beagle", "Dachshund", "Yorkshire Terrier", "Great Dane", "Bichon Frise", "Bernese Mountain Dog"]

def create_stores():
    print("Deleting existing stores...")
    session.query(Store).delete()
    session.commit()

    print("New stores generating...")

    stores = []
    for store in pet_stores:
        item = Store(
            name = store,
            address=fake.address()
        )
        stores.append(item)
    session.add_all(stores)
    session.commit()
    return stores

def create_pet_items():
    print("Deleting existing pets...")
    session.query(PetItem).delete()
    session.commit()

    print("Creating new pets...")
    pet_items = []
    for breed in pets:
        item = PetItem(
            name = breed,
            quantity=randint(0, 10),
            unit_price=randint(200, 5000)
        )
        pet_items.append(item)
    session.add_all(pet_items)
    session.commit()
    return pet_items

def create_shopping_carts(pet_items, stores):
    print("Deleting existing shopping cart...")
    session.query(ShoppingCart).delete()
    session.commit()

    print("Creating a new shopping cart for you!")
    
    # shoppingcarts = [ShoppingCart(store=rc(stores)) for i in range(50)]
    shopping_carts = []
    for i in range(25):
        store = rc(stores)
        random_pet_items = [rc(pet_items) for i in range(10)]
        for item in random_pet_items:
            if not item in store.pet_items:
                store.pet_items.append(item)
        shopping_carts.append(ShoppingCart(store=store))
    session.add_all(shopping_carts)
    session.commit()
    return shopping_carts

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