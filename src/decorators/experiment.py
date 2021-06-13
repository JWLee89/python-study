"""
@Author Jay Lee
Here, we will get funky with decorators
and learn to handle decorating class methods
and or functions
"""
import typing as t
from functools import wraps


def handle_method(func: t.Callable,
                  *args: t.Tuple) -> t.Tuple:
    """
    This will return self or cls
    based on whether the given function is a

    - method - return self
    - classmethod - return cls

    Other methods will return None as the first item
    in the tuple

    Args:
        func (t.Callable): The function to be evaluated
        *args (t.Tuple): Arguments passed by the consumer

    Returns:
        (t.Tuple): A two-tuple with the following specifications:
            - (self, *args) if func is a method
            - (cls, *args) if func is a classmethod
            - (None, *args) if func is a staticmethod or a function
        """
    if func:
        # All
        self = getattr(func, '__self__', None)
        # print(dir(func))
        print(f"Self: {self}, qual_name: {func.__qualname__}, "
              f"")
        if self:
            self, args = args[0], args[1:]
            return self, args
    return None, args


def handle_func_or_method(num_arg: int):

    def inner(func_to_wrap: t.Callable) -> t.Callable:
        """
        
        Args:
            func_to_wrap (t.Callable): The function that we
            will be wrapping

        Returns:
            (t.Callable): A function that performs some actions before outputting
            the output of func_to_wrap

        """
        @wraps(func_to_wrap)
        def returned_func(*args, **kwargs):
            print(f"i run before func. num_arg: {num_arg}")
            cls_or_self, new_args = handle_method(func_to_wrap, *args)
            if cls_or_self:
                print(f"cls_or_self is not None: {cls_or_self}")
                return func_to_wrap(cls_or_self, *new_args, **kwargs)
            return func_to_wrap(*args, **kwargs)
        return returned_func
    return inner


if __name__ == "__main__":
    class Cls:
        def __init__(self):
            self.a = 1

        @handle_func_or_method(10)
        def method(self):
            return self.a

    # @handle_func_or_method(10)
    def func():
        return 1

    a = Cls()
    print(a.method())
