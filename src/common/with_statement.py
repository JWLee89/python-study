from contextlib import contextmanager


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
        yield file
        print("Temporarily suspended. You won't see me until file closes ... ")
    finally:
        if file:
            print("Closing the file ... ")
            file.close()


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
