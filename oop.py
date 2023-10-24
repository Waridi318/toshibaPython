class Fruits:
    def __init__(self, type, price, color):
        self.type = type
        self.price = price
        self.color = color

    def onyesha(self):
        print(f"I like eating {self.type} and it cost {self.price}, color being {self.color}")


# creating an object

myobj = Fruits("banana", "20 Ksh", "yellow")

myobj.onyesha()
