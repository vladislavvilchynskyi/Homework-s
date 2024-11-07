class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f'{self.dimensions} {self.name}, price -> {self.price} '

class User:

    def __init__(self, name, surname, numberphone, age):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone
        self.age = age

    def __str__(self):
        return f'{self.name} {self.surname}, age -> {self.age}\nPhone number -> {self.numberphone}'


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        items_str = '\n'.join([f"{item.name} -> {cnt} pcs. " for item, cnt in self.products.items()])
        return f'User: \n{self.user}\n\nItems:\n{items_str}\n\nTotal price:\n{self.get_total()}'

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162", "23")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40