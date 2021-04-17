
def test_upacking():
    dict_item = {'y': 1, 'x': 2, 'z': 3}
    # Print keys
    print(*dict_item)
    # print items:
    dict_item = {'yee': 1, 'xee': 2, 'zee': 3}

    # invalid key
    try:
        print(**dict_item)
    except TypeError as ex:
        print(ex)


if __name__ == "__main__":
    test_upacking()
