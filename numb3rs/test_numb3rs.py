from numb3rs import validate

def main():
    test_valid()
    test_alphabet()
    test_dot()
    test_length()

def test_valid():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("256.23.67.65") == False

def test_alphabet():
    assert validate("cat") == False
    assert validate("a.b.c.d") == False

def test_dot():
    assert validate("1?2.3:4") == False

def test_length():
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False

if __name__ == "__main__":
    main()
