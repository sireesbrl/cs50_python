import sys

if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

elif not sys.argv[1].endswith(".py"):
    print("Not a Python file")
    sys.exit(1)

else:
    try:
        with open(sys.argv[1]) as file:
            count = 0
            for lines in file:
                if not lines.lstrip().startswith("#") and not lines.strip() == "":
                    count += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    else:
        print(count)
