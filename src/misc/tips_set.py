

if __name__ == "__main__":
    """
    Be sure to use the appropriate data structure for doing tasks such
    as calculating the intersection between two sets
    """
    set_1 = [1, 3, 5, 7, 9]
    set_2 = [2, 3, 4, 5, 6]

    union = []
    # slow way
    for x in set_1:
        for y in set_2:
            if x == y:
                union.append(x)

    print(f"Union: {union}")

    # Better way
    union = set(set_1) & set(set_2)
    print(f"Union: {union}")
