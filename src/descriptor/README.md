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
