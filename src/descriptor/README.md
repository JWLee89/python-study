## Descriptor

This will be a brief post on descriptors. Below is a 
definition of dsecriptors taken out of [Fluent Python](https://amzn.to/3pLx7cu).

>A descriptor is a `class` that implements a protocol 
>(fancy word for a set of rules) consisting of the
>`__get__`, `__set__` and `__delete__` methods.
> As usual with protocols, partial implementations are okay.

Partial implementations are okay. Most real-world descriptors 
only implement the `__get__` and `__set__` property, or even 
just one of the two. 

For example, if you want to prevent users from setting invalid 
values to a property, simply overwriting `__set__` will suffice. 
Let's take a look at a code snippet. 

```python
class A:
    def __init__(self):
        self.a = 10

    def __repr__(self):
        return str(self.a)


if __name__ == "__main__":
    instance = A()

    # Going through the various ways
    # of setting property values
    instance.a = 20
    print(instance)

    # Same as above
    instance.__dict__['a'] = 30
    print(instance)

    # Same as above
    setattr(instance, 'a', 40)
    print(instance)
    
    # But are they really the same?
```

The code snippet above shows three "different" ways of 
retrieving an attribute from a class instance. 

Descriptors are a great way of reducing boilerplate code, 
especially when we have data attributes of the same type that 
require the same sanity check. The code below is a simple example of 
the descriptor protocol implemented by the `Quantity` class. 
The code snippet is also available under `descriptor.py`

```python
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
```
