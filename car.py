class Car:
    color="Black"
    def __init__(self,name,price):
     self.name=name
     self.price=price

    def achievements(self):
        return f"I'm driving a new {self.name} car"

    def amount(self):
        return f"The car goes for ${self.price}"

