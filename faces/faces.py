#converts emoticons in a text into its corresponding emoji

def convert(text):
    for i in range(len(text)):
        if ':)' in text[i]:
            text[i] = '🙂'
        elif ':(' in text[i]:
            text[i] = '🙁'
        else:
            continue

def main():
    text = input("Enter a text(with emoticons): ").split()
    convert(text)
    for i in range(len(text)):
        if i <len(text) - 1:
            print(text[i] + " ", end = "")
        else:
            print(text[i])

main()
