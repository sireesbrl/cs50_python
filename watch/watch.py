import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe (.+)><\/iframe>", s):
        if url := re.search(r"http(?:s)?:\/\/(?:www\.)?youtube\.com\/embed\/(\w+)", s):
            return f"https://youtu.be/{url.group(1)}"
    else:
        return None





if __name__ == "__main__":
    main()
