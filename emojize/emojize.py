import emoji

text = input("Input: ").strip()

print(f"Output: {emoji.emojize(text, language = "alias")}")
