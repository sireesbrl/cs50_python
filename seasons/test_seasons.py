from seasons import check_date

def main():
    test_date()

def test_date():
    assert check_date("2000-06-21") == (2000,6,21)
    assert check_date("June 21, 2000") == None
    assert check_date("2000-6-21") == None

if __name__ == "__main__":
    main()
