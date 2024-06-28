import random


def main():
    level = get_level()
    get_rounds(level)


def get_rounds(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        ans =  check_ans(x, y)
        if ans == True:
            score += 1
            count_round += 1
        else:
            count_round += 1
    print(f"Score: {score}")


def check_ans(x, y):
    tries = 1
    while tries <= 3:
        try:
            ans = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
            continue
        else:
            if ans == (x + y):
                return True
            else:
                tries += 1
                print("EEE")
                continue
    print(f"{x} + {y} = {x + y}")
    return False


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
        except ValueError:
            continue
        else:
            if not level in [1, 2, 3]:
                continue
            else:
                return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y



if __name__ == "__main__":
    main()
