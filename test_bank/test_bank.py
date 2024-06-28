from bank import value

def main():
    test_hello()
    test_start_with_h()
    test_else()

def test_hello():
    assert value("hello") == 0


def test_start_with_h():
    assert value("Hey?") == 20

def test_else():
    assert value("What's hapenning?") == 100



if __name__ == "__main__":
    main()
