class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other
        elif isinstance(other, float):
            return self.price + other
        
    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            return self.price - other
        elif isinstance(other, float):
            return self.price - other
        
    def __mul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other, int):
            return self.price * other
        elif isinstance(other, float):
            return self.price * other
        
    def __truediv__(self, other):
        if isinstance(other, Item):
            return self.price / other.price
        elif isinstance(other, int):
            return self.price / other
        elif isinstance(other, float):
            return self.price / other
    



item_1 = Item('Видеокарта', 15000, 0.8)
item_2 = Item('Процессор', 12000, 0.3)

total_price = item_1.price + item_2.price
print(total_price)

new_total_price = item_1 + 1000
print(new_total_price)

example = item_1.price * item_2.price
print(example)

example = item_1 * item_2
print(example)

example = item_1.price / item_2.price
print(example)

example = item_1 / item_2
print(example)