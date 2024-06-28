import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

elif not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)

else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            menu = []
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    else:
        print(tabulate(menu[1:], headers = menu[0], tablefmt = "grid"))
