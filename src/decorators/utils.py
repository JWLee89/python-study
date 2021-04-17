import time
import numpy as np


def upper(func):
    def wrapper(input_str):
        original_result = func(input_str)
        modified_res = original_result.upper()
        return modified_res
    return wrapper


class ComputeTime:
    def __init__(self, func):
        self.func = func
        self.time = []

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        output = self.func(*args, **kwargs)
        time_elapsed = time.time() - start_time
        self.time.append(time_elapsed)
        return output

    def compute_time(self):
        return np.mean(self.time) / 1000


def compute_time_ms(func):
    """
    Decorator for computing the amount of time taken to do something
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        original_result = func(*args, **kwargs)
        time_elapsed = time.time() - start_time
        print(f"Time taken: {time_elapsed * 1000}")
        return original_result
    return wrapper


@compute_time_ms
def greet(input_str):
    return input_str


if __name__ == "__main__":
    print(greet("hello world"))
