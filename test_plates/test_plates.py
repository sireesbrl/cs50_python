from plates import is_valid

def main():
    test_length()
    test_zero_placement()
    test_numbers_placement()
    test_special_characters()

def test_length():
    assert is_valid("C") == False
    assert is_valid("CS") == True
    assert is_valid("ABCDEFGHIJKLMNOP") == False

def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_numbers_placement():
    assert is_valid("50CS") == False
    assert is_valid("AAA22A") == False
    assert is_valid("123456") == False
    assert is_valid("AAA222") == True

def test_special_characters():
    assert is_valid(".,?!") == False
    assert is_valid(" CS 50 ") == False
    assert is_valid("PI3.14") == False


if __name__ == "__main__":
    main()
