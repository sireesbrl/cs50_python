#list of vowels
vowels = ["a", "e", "i", "o", "u",
          "A", "E", "I", "O", "U"]

word = input("Input: ").strip()

while True:
    for i in range(len(word)):
        if word[i] in vowels:
            word = word.replace(word[i], "")
            #if it contains vowel, break loop to get new length of word
            break
    #if no vowels in word, break loop and print as it is
    if not any(vowel in word for vowel in vowels):
        break

print(word)
