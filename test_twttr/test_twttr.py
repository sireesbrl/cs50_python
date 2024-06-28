from twttr import shorten

def main():
    test_case()
    test_numbers()
    test_punctuation()

def test_case():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("bcd") == "bcd"

def test_numbers():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten(".,?!") == ".,?!"


if __name__ == "__main__":
    main()
