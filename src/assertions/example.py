
def this_should_raise_error():
    assert 1 != 2, "Should never see this message since this test should always pass. "
    print("Okay we established the obvious")
    assert (1 == 2, 'should always fail')
    print("Why is there no error?")
    print("")


if __name__ == "__main__":
    this_should_raise_error()