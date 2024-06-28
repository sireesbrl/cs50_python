from project import start_page, acc_exists, check_login
from menu import check_edit_disciples, check_delete_disciples
from disciples import Disciples
from unittest.mock import patch
import os


# check if user has an account
def test_start_page():
    with patch("builtins.input", return_value="yes"):
        assert start_page() == True
    with patch("builtins.input", return_value="no"):
        assert start_page() == False


# check if given account exists already during sign up
def test_acc_exists():
    assert acc_exists("test1") == True
    assert acc_exists("xyz") == False


# check if account exists during login
def test_check_login():
    assert (
        check_login(
            "test1", "1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014"
        )
        == "M"
    )
    assert check_login("xyz", "password") == None


# check if given data is valid and written to file properly
def test_check_add_data():
    disciple1 = Disciples()
    assert disciple1.check_add_data("Test1","Outer", "Qi refinement", "Warrior", "Combat", "Wood") == True
    disciple2 = Disciples()
    assert disciple2.check_add_data("abc", "def", "ghi", "jkl", "mno", "pqr") == False


# check if data is properly read from file
def test_check_read_data():
    assert Disciples.check_file_reader() == [
        {
            "Name": "Test1",
            "Disciple_type": "Outer",
            "Level": "Qi refinement",
            "Profession": "Warrior",
            "Department": "Combat",
            "Cultivation_law": "Wood",
        }
    ]


# check if data can be edited in a file properly
def test_check_edit_data():
    assert (
        check_edit_disciples(
            "Test1", "Inner", "Core formation", "Warrior", "Combat", "Fire"
        )
        == True
    )
    assert (
        check_edit_disciples(
            "Test2", "Core", "Nascent soul", "Alchemist", "Alchemy", "Wood"
        )
        == False
    )


# check if data can be deleted from file properly
def test_check_delete_data():
    assert check_delete_disciples("Test1") == True
    assert check_delete_disciples("Test2") == False
    os.remove("test_disciples.csv")



def main():
    test_start_page()
    test_acc_exists()
    test_check_login()
    test_check_add_data()
    test_check_read_data()
    test_check_edit_data()
    test_check_delete_data()


if __name__ == "__main__":
    main()
