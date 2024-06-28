def main():
    frac = input("Fraction: ").strip()
    try:
        fuel = gauge(convert(frac))
    except ValueError:
        pass
    else:
     print(fuel)


def convert(fraction):
    x_temp, y_temp = fraction.split("/")
    x = int(x_temp)
    y = int(y_temp)
    try:
        return round((x/y) * 100)
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
