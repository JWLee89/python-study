from collections import namedtuple
"""
Named tuples can be a great alternative classes
especially if the class is designed to simply hold data.
For example the following
"""
Person = namedtuple("Person", ["age", "height"])

if __name__ == "__main__":
    bob = Person(28, 180)
    print(bob)
