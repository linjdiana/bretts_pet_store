from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///pet_stores.db')

Base = declarative_base()

pet_item_store = Table(
    'pet_item_stores',
    Base.metadata,
    Column('pet_item_id', ForeignKey('pet_items.id'), primary_key=True),
    # store ID
    Column('store_id', ForeignKey('stores.id'), primary_key=True),
    #Column('quantity_purchased', ForeignKey('quantity_purchased'), primary_key=True)
)

class PetItem(Base):
    __tablename__ = 'pet_items'

    id = Column(Integer(), primary_key=True)
    name = Column(String(25), index = True)
    quantity = Column(Integer())
    price = Column(Float())
    unit_price = Column(Float())

    def __repr__(self):
        return f'PetItem(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'price={self.price})'
    
class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    address = Column(String())

    shopping_carts = relationship('ShoppingCart', backref=backref('store'))
    grocery_items = relationship('PetItem', secondary=pet_item_store, back_populates='stores')

    pet_items = relationship('Pet_item', backref=backref('store'))


    def __repr__(self):
        return f'Store(id={self.id}), ' + \
            f'name={self.name}'
    
    ## what do we do with the one shopping cart? 