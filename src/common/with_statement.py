
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


if __name__ == "__main__":
    with_example()
