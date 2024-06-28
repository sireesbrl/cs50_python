import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    address = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    if address and  check_number(address):
        return True
    else:
        return False


def check_number(address):
    if 0<=int(address.group(1))<=255 and 0<=int(address.group(2))<=255 and 0<=int(address.group(3))<=255 and 0<=int(address.group(4))<=255:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
