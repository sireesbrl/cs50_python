def main():
    text = input("Input: ").strip()
    print(shorten(text))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    for letters in word.lower():
        if letters in vowels:
            word = word.replace(letters, "")
    return word


if __name__ == "__main__":
    main()
