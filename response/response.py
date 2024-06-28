from validator_collection import validators

def main():
    email_address = input("What's your email address? ")
    try:
        validators.email(email_address)
    except:
        print("Invalid")
    else:
        print("Valid")


if __name__ == "__main__":
    main()
