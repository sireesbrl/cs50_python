from datetime import date
import sys
import inflect
import re

def main():
    try:
        year, month, day = check_date(input("Date of Birth: ").strip())
    except:
        sys.exit("Invalid Date")
    else:
        mins = ((date.today() - date(year, month, day)).days * 24 * 60)
    p = inflect.engine()
    output = p.number_to_words(mins, andword = "")
    print(f"{output.capitalize()} minutes")

def check_date(date_of_birth):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", date_of_birth):
        year, month, day = date_of_birth.split("-")
        return (int(year), int(month), int(day))


if __name__ == "__main__":
    main()
