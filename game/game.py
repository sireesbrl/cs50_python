import random

while True:
    try:
        n = int(input("Level: ").strip())
    except ValueError:
        continue
    else:
        if n <= 0 or n > 100:
            continue
        else:
            break

num = random.randint(1,n)

while True:
    try:
        guess = int(input("Guess: ").strip())
    except ValueError:
        continue
    else:
        if guess < 0:
            continue
        else:
            if guess == num:
                print("Just right!")
                break
            elif guess > num:
                print("Too large!")
            elif guess < num:
                print("Too small!")




