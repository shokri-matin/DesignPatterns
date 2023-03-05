class Product:

    id = 0
    name = ""
    price = 0

    def __init__(self, id, name, price):

        self.id = id
        self.name = name
        self.price = price

        print("Inital product with id:{}, name:{}, price:{}".format(id, name, price))

    def getName(self):
        
        print("Product name is {}".format(self.name))

    def getPrice(self):

        print("Product price is {}".format(self.price))


