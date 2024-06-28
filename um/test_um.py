from um import count

def main():
    test_case()
    test_word()
    test_spaces()


def test_case():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_word():
    assert count("yummy") == 0

def test_spaces():
    assert count("hello um world") == 1

if __name__ == "__main__":
    main()
