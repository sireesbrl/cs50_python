import math

def get_frac():
    while True:
        try:
            frac = input("Fraction: ").strip().split("/")
            x = frac[0]
            y = frac[1]
        except not x.is_integer() or not y.is_integer() or int(x)/int(y) == ZeroDivisionError:
            pass
        else:
            try:
                return int(x), int(y)
            except ValueError:
                pass

def main():
    while True:
        x, y = get_frac()
        if x  > y or y == 0:
            continue
        else:
            break

    if (x/y)*100 <= 1.0:
        print("E")
    elif (x/y)*100 >= 90.0:
        print("F")
    else:
        print(f"{math.ceil((x/y)*100)}%")


main()
