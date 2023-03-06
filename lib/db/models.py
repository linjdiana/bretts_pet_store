from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# pet_item_store = Table(
#     'pet_item_stores',
#     Base.metadata,
#     Column('pet_item_id', ForeignKey('pet_items.id'), primary_key=True),
#     # store ID
#     Column('store_id', ForeignKey('stores.id'), primary_key=True),
#     #Column('quantity_purchased', ForeignKey('quantity_purchased'), primary_key=True)
# )

# class PetItem(Base):
#     __tablename__ = 'pet_items'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String())
#     quantity = Column(Integer())
#     price = Column(Float())
#     unit_price = Column(Float())