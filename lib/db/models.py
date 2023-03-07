from sqlalchemy import create_engine, func
from sqlalchemy import PrimaryKeyConstraint, ForeignKey, Table, Column, Integer, Float, String
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
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    quantity = Column(Integer())
    unit_price = Column(Float())
    store_id = Column(Integer(), ForeignKey('stores.id'))

    shopping_cart_id = Column(Integer(), ForeignKey('shopping_carts.id'))
    # stores = relationship('Store', secondary=pet_item_store, back_populates='grocery_items')

    def __repr__(self):
        return f'PetItem(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'unit_price={self.unit_price})'
    
class Store(Base):
    __tablename__ = 'stores'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    address = Column(String())

    # shopping_carts = relationship('ShoppingCart', backref=backref('store'))
    # pet_items = relationship('PetItem', backref=backref('stores'))

    def __repr__(self):
        return f'Store(id={self.id}), ' + \
            f'name={self.name}' + \
            f'address={self.address}'
    
    ## what do we do with the one shopping cart? 
class ShoppingCart(Base):
    __tablename__ = 'shopping_carts'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    store_id = Column(Integer(), ForeignKey('stores.id'))
    
    def __repr__(self):
        return f'ShoppingCart(id={self.id})'

# different table that keeps track of all the stuff that goes into the shopping cart ((jointable)) 
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    pet_item_id = Column(Integer(), ForeignKey('pet_items.id'))
    shopping_cart_id = Column(Integer(), ForeignKey('shopping_carts.id'))
    def __repr__(self):
        return f'Order ID: {self.id}' \
            + f'Pet Item ID: {self.pet_item_id}' \
            + f'Shopping Cart ID: {self.shopping_cart_id}'

