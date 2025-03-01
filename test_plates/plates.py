def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False

if __name__ == "__main__":
    main()
