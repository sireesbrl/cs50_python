from working import convert
import pytest


def main():
    test_time()
    test_format()
    test_hrs()
    test_mins()


def test_time():
    assert convert("5 AM to 9 PM") == "05:00 to 21:00"
    assert convert("10 PM to 9 AM") == "22:00 to 09:00"
    assert convert("5:45 PM to 9:30 AM") == "17:45 to 09:30"

def test_format():
    with pytest.raises(ValueError):
        convert("5 AM - 9 PM")

def test_hrs():
    with pytest.raises(ValueError):
        convert("5 AM to 20 PM")

def test_mins():
    with pytest.raises(ValueError):
        convert("5:60 AM to 8:60 PM")


if __name__ == "__main__":
    main()
