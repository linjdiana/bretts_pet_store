from db.models import PetItem, Order
from rich.console import Console
console = Console()

YES = ['y', 'ye', 'yes']
NO = ['n', 'no']

def create_store_table(stores):
    console.print('[teal]-' * 50)
    console.print(f'[bold purple]|ID  |NAME{" " * 39}|')
    console.print('[teal]-' * 50)
    for store in stores:
        id_spaces = 4 - len(str(store.id))
        name_spaces = 43 - len(store.name)
        console.print(f'[cyan]|{store.id}{" " * id_spaces}|{store.name}{" " * name_spaces}|')
    console.print('[teal]-' * 50)

def create_pet_item_table(pet_items):
    print('-' * 50)
    console.print(f'[bold purple]|ID  |PET NAME{" " * 24}|PRICE{" " * 4}|')
    print('-' * 50)
    for pet_item in sorted(pet_items, key=lambda g: g.id):
        id_spaces = 4 - len(str(pet_item.id))
        name_spaces = 33 - len(pet_item.name)
        price_spaces = 8 - len(f'{pet_item.unit_price:.2f}')
        output_string = f'|{pet_item.id}{" " * id_spaces}|' + \
            f'{pet_item.name}{" " * name_spaces}|' + \
            f'${pet_item.unit_price:.2f}{" " * price_spaces}|'
        console.print(f'[cyan]{output_string}')
    print('-' * 40)

# def fill_cart(session, store):
#     shopping_cart = Order(store=store)
#     pet_item_id = input('Please enter the ID of your first item: ')
#     cart_total = 0
#     while pet_item_id:
#         pet_item = session.query(PetItem).filter(
#             PetItem.id==pet_item_id).first()
#         if pet_item in store.pet_items:
#             shopping_cart.grocery_items.append(pet_item)
#             cart_total += pet_item.unit_price
#             print(f'Your item is ${cart_total:.2f}\n')
#         else:
#             pet_item_id = input('Please enter a valid pet item ID: ')
#             continue

#         # yes_no = None
#         # while yes_no not in YES + NO:
#         #     yes_no = input('Would you like to add another item to your cart? (Y/n) ')
#         #     if yes_no.lower() in YES:
#         #         grocery_item_id = input('Please enter the ID of your next item: ')
#         #     elif yes_no.lower() in NO:
#         #         grocery_item_id = None

#     return shopping_cart, cart_total

# def show_cart(shopping_cart):
#     print('-' * 50)
#     print(f'|ID  |NAME{" " * 29}|PRICE{" " * 4}|')
#     print('-' * 50)
#     for pet_item in sorted(shopping_cart.grocery_items, key=lambda g: g.id):
#         id_spaces = 4 - len(str(pet_item.id))
#         name_spaces = 33 - len(pet_item.name)
#         price_spaces = 8 - len(f'{pet_item.unit_price:.2f}')
#         output_string = f'|{pet_item.id}{" " * id_spaces}|' + \
#             f'{pet_item.name}{" " * name_spaces}|' + \
#             f'${pet_item.unit_price:.2f}{" " * price_spaces}|'
#         print(output_string)
#     cart_total = sum([g.price for g in shopping_cart.grocery_items])
#     total_spaces = 8 - len(str(cart_total))
#     print(f'|{" " * 5}TOTAL{" " * 28}|${cart_total:.2f}{" " * total_spaces}|')
#     print('-' * 50)

# # def remove_from_cart(session, shopping_cart, cart_total):
# #     yes_no = input('Would you like to remove any items from your cart? (Y/n) ')
# #     while yes_no in YES:
# #         pet_item_id = input('Please enter the ID of the item you would like to remove: ')
# #         grocery_item = session.query(PetItem).filter(
# #             PetItem.id==pet_item_id).first()
# #         if grocery_item in shopping_cart.grocery_items:
# #             shopping_cart.grocery_items.remove(grocery_item)
# #             cart_total -= grocery_item.price
# #         else:
# #             print('Item not found.')
# #         print('Here are the items in your cart:')
# #         show_cart(shopping_cart)

# #         yes_no = input('Would you like to remove another item from your cart? (Y/n) ')

# def collect_payment(cart_total):
#     paid = False
#     while not paid:
#         payment_method = input(f'Will you be paying with cash or card? ')
#         if payment_method.lower() == 'card':
#             print('Processing...\n')
#             paid = True
#         elif payment_method.lower() == 'cash':
#             payment = input('How much will you be paying with today? ' )
#             try:
#                 payment = float(payment)
#                 change = payment - cart_total
#                 if (change > 0):
#                     print(f'Your change is ${change:.2f}\n')
#                 paid = True
#             except:
#                 print('Please enter a valid number.')
#         else:
#             print('Please select a valid payment method.')
