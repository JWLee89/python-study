import typing as t


def quantity(name: str):
    """
    Create a quantity property, which by definition is:
    1. A positive Integer (>= 0)
    Args:
        instance (): The object instance to attach
        the property to
        name (): The name of the property
    Returns:

    """
    def getter(instance: t.Any) -> int:
        """
        Get the item from the instance
        """
        return instance.__dict__[name]

    def setter(instance, new_value: int):
        if not isinstance(new_value, int):
            raise TypeError("New value must be an integer")

        if new_value < 0:
            raise ValueError("'new_value' must be greater than "
                             "or equal to 0")
        instance.__dict__[name] = new_value

    return property(getter, setter)


class StoreItem:
    qty = quantity('quantity')

    def __init__(self, item_count):
        self.qty = item_count


if __name__ == "__main__":
    item = StoreItem(10)
    try:
        error_item = StoreItem(10.5)
    except TypeError as ex:
        print("New value is a float ... ")
        print(ex)
