from designs import get_header, clr_screen, delay, greet
from getpass import getpass
from typing import Union
import hashlib
import csv
import menu

def has_acc_or_not() -> bool:
    while True:
        exists: str = input("Do you have an account (yes/no)? ").strip().lower()
        if exists in ["yes", "y"]:
            has_acc = True
            break

        elif exists in ["no", "n"]:
            has_acc = False
            break
        else:
            print("Invalid!")
            delay(2)
            continue
    return has_acc

def start_page() -> bool:
    clr_screen()
    get_header()
    if has_acc_or_not():
        return True
    else:
        return False


def acc_exists(user_name) -> bool:
    exists = False
    with open("accounts.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get("user_name") == user_name:
                exists = True
                break
    return exists

def sign_up() -> bool:
    clr_screen()
    get_header()
    while True:
        print("Sign up:")
        account_type: str = (
            input(
                "Enter account type [Sect (M)aster, (V)ice-Sect Master, Sect-(P)rotector, (D)isciple]: "
            )
            .strip()
            .upper()
        )

        if not account_type in ["M", "V", "P", "D"]:
            print("Invalid! Enter M, V, P or D")
            delay(2)
            clr_screen()
            get_header()
            continue
        if account_type == "M":
            permission = "M"
            break
        if account_type == "V":
            permission = "V"
            break
        if account_type == "P":
            permission = "P"
            break
        if account_type == "D":
            permission = "D"
            break
    user_name: str = input("Username: ").strip()
    if acc_exists(user_name):
        print("User already exists!")
        delay(2)
        sign_up()
    else:
        password: str = hashlib.sha256(getpass().encode()).hexdigest()
        account = {"user_name": user_name, "password": password, "permission": permission}
        with open("accounts.csv", "a") as file:
            writer = csv.DictWriter(
                file, fieldnames=["user_name", "password", "permission"]
            )
            writer.writerow(account)
        print("Account created successfully!")
        delay(2)
    return True


def check_login(user_name, password) -> Union[str, None]:
    with open("accounts.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get("user_name") == user_name and row.get("password") == password:
                permission = row.get("permission")
                break
            else:
                permission = None
    return permission

def login() -> Union[str, None]:
    clr_screen()
    get_header()
    print("Login:")
    user_name: str = input("Username: ").strip()
    password: str = hashlib.sha256(getpass().encode()).hexdigest()
    permission: Union[str, None] = check_login(user_name, password)
    if not isinstance(permission, str):
        return None
    return permission

def file_exists() -> bool:
    with open("accounts.csv") as file:
        reader = csv.DictReader(file)
        try:
            next(reader)
        except StopIteration:
            return False
    return True


def main():
    clr_screen()
    greet()
    if not file_exists():
        print("No account registered")
        delay(2)
        sign_up()

    if start_page():
        permission: Union[str, None] = login()
    else:
        sign_up()
        permission = login()
    menu.options_available(permission)


if __name__ == "__main__":
    main()
