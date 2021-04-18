from contextlib import contextmanager
import time
from typing import List


def with_example():
    with open('dummy.txt', 'r') as file:
        print(file.read())

    # Is similar to as follows but much shorter
    try:
        file = open('dummy.txt', 'r')
        print(file.read())
    finally:
        if file and not file.closed:
            file.close()


# From Python Tricks. Really good example
class ManagedFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        """
        Returned when using with ManagedFile(name, 'r') as file
        :return: the file (output of open
        :rtype:
        """
        print("Runs when the code executes with() block")
        self.file = open(self.name, self.mode)
        print(f"Opened file ... {self.name} in '{self.mode}' mode")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print("Exiting with() context. File closing ... yee ... ")
            self.file.close()


@contextmanager
def managed_file(name, mode):
    """
    Fortunately, we can create our own context managers without having
    to do what we did above.

    Questions to ask.
    1. What does the contextmanager decorator do?
    2. Why do we need to add a 'yield' statement?
        - Do functions decorated with contextmanager output a generator? Yep that's right.
    """
    file = None
    try:
        file = open(name, mode)
        print("Opened the file. Exiting the function so that with statement body runs")
        yield file
        print("Temporarily suspended. You won't see me until file closes ... ")
    finally:
        if file:
            print("Closing the file ... ")
            file.close()


class TimeComputer:
    class Units:
        MS = 'milliseconds'

    def __init__(self, accumulated_time: List) -> None:
        if not isinstance(accumulated_time, list):
            raise TypeError(f"accumulated_time must be a list. "
                            f"Passed in type: {type(accumulated_time)}")
        self.accumulated_time = accumulated_time

    def __enter__(self) -> None:
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        time_elapsed = time.time() - self.start_time
        self.accumulated_time.append(time_elapsed)

    @staticmethod
    def compute_avg_time(time_list: List, unit: str = None) -> float:
        avg_time = sum(time_list) / len(time_list)
        if unit == TimeComputer.Units.MS:
            avg_time *= 1000
        return avg_time



class Indenter:
    def __init__(self):
        self.indent_level = -1

    def __enter__(self):
        self.indent_level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.indent_level != 0:
            self.indent_level -= 1

    def print(self, *item):
        print('   ' * self.indent_level, *item)


if __name__ == "__main__":
    with_example()
    file_name, mode = 'dummy.txt', 'r'

    # We can create our own context class
    with ManagedFile(file_name, mode) as file:
        print(file.read())

    print("-" * 100)
    # Context manager example
    with managed_file(file_name, mode) as file:
        print(file.read())

    print("-" * 100)

    # Implement our own indenter:
    with Indenter() as indent:
        print(indent)
        indent.print('captain', 'yee')
        with indent:
            indent.print('teemo')
            with indent:
                indent.print('on duty!')
            indent.print("yee")

    time_elapsed_ms = []
    for i in range(100):
        with TimeComputer(time_elapsed_ms) as tc:
            items = list(range(100000))

    print(f"Avg time elapsed: {TimeComputer.compute_avg_time(time_elapsed_ms, unit=TimeComputer.Units.MS)}")