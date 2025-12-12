class Product:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Товар: '{self.title}', Цена: {self.price} сом, В наличии: {self.quantity} шт."

    def __repr__(self):
        return f"Product(title='{self.title}', price={self.price}, quantity={self.quantity})"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.title == other.title
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Product):
            new_title = "Combo"
            new_price = self.price + other.price
            new_quantity = 1
            return Product(title=new_title, price=new_price, quantity=new_quantity)
        raise TypeError(f"Невозможно сложить 'Product' с типом '{type(other).__name__}'")

p1 = Product("Клавиатура", 1500, 10)
p2 = Product("Клавиатура", 1800, 5)
p3 = Product("Мышка", 700, 20)

print(p1 == p2)
print(p3 < p1)
combo = p1 + p3
print(combo)
