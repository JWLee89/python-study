"""
@Author Jay Lee.
We will refactor quantity to implement the descriptor protocol.
The descriptor protocol is a fancy word that partially implements
the following methods:

- __delete__
- __get__
- __set__

The example below is from "Fluent Python".
This book is extremely useful for digging into Python.
If you want to take your Python skills to the next level,
please support the authors.

Note that I am not affiliated with the author in any way.
I just think that this book is awesome!
"""


class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value >= 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError("Value must be >= 0")


class LineItem:
    weight = Quantity("weight")
    price = Quantity("price")

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"description: {self.description}, " \
               f"weight: {self.weight}, " \
               f"price: {self.price}"


if __name__ == "__main__":
    weight, price = 10, 20
    flower = LineItem("a flower ...", weight, price)

    weight, price = 10, -9999
    try:
        flower = LineItem("a flower ...", weight, price)
    except ValueError:
        print("error raised due to invalid price")
