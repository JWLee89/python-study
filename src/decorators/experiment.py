"""
@Author Jay Lee
Here, we will get funky with decorators
and learn to handle decorating class methods
and or functions
"""
import typing as t
from functools import wraps


def handle_method(function_to_evaluate: t.Callable,
                  args: t.Tuple) -> t.Tuple:
    """
    This will return self or cls
    based on whether the given function is a

    - method - return self
    - classmethod - return cls

    Other methods will return None as the first item
    in the tuple

    Args:
        function_to_evaluate (t.Callable): The function to be evaluated
        *args (t.Tuple): Arguments passed by the consumer

    Returns:
        (t.Tuple): A two-tuple with the following specifications:
            - (self, *args) if func is a method
            - (cls, *args) if func is decorated with @classmethod
            - (None, *args) if func is a staticmethod or a function
        """
    # If tuple is empty, we do not even need to evaluate,
    # since classmethod or method has at least one argument
    if len(args):
        self_or_cls = args[0]
        # Bound methods can be accessed by cls_or_class.<name-of-method>
        method = getattr(self_or_cls, function_to_evaluate.__name__, None)
        if method:
            wrap = getattr(method, "__func__", None)
            original = getattr(wrap, "original", None)
            if original is function_to_evaluate:
                return self_or_cls, args[1:]
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
        desc = next((desc for desc in (staticmethod, classmethod)
                     if isinstance(func_to_wrap, desc)), None)
        if desc:
            func_to_wrap = func_to_wrap.__func__

        @wraps(func_to_wrap)
        def returned_func(*args, **kwargs):
            cls_or_self, new_args = handle_method(func_to_wrap, args)
            print('class: %-10s func: %-15s args: %-10s kwargs: %-10s' %
                  (cls_or_self, func_to_wrap.__name__, new_args, kwargs))

            # Handle case where self exists
            if cls_or_self:
                return func_to_wrap(cls_or_self, *new_args, **kwargs)
            return func_to_wrap(*args, **kwargs)

        returned_func.original = func_to_wrap

        if desc:
            returned_func = desc(returned_func)
        return returned_func
    return inner


class Cls:
    def __init__(self):
        self.a = 1

    @handle_func_or_method(10)
    @classmethod
    def method(cls):
        print(f"self: {cls}")
        return 250

    def __repr__(self):
        return f"Cls. a: {self.a}"


if __name__ == "__main__":

    # @handle_func_or_method(10)
    def yeeee():
        return 1

    a = Cls()
    print(a.method())
