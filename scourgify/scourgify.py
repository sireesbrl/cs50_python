import sys
import csv

def check_command_line():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    else:
        return True


def read_file():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            table = []
            for row in reader:
                name = row["name"].split(",")
                table.append({"first": name[1].lstrip(), "last": name[0], "house": row["house"]})

    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

    else:
        return table

def write_file(table):
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        writer.writerows(table)


def main():
    if check_command_line():
        write_file(read_file())


if __name__ == "__main__":
    main()


