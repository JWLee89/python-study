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
