class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getName(self):
        print(self.name)

    def getPrice(self):
        print(self.price)


num_products = int(input("Enter how many products: "))
products = []

for i in range(num_products):
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    p = Product(name, price)
    products.append(p)

for p in products:
    p.getName()
    p.getPrice()
