import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)$", s)
    if time:
        if int(time.group(1)) > 12 or int(time.group(4)) > 12:
            raise ValueError
        else:
            time1 = new_time(time.group(1), time.group(2), time.group(3))
            time2 = new_time(time.group(4), time.group(5), time.group(6))
            return f"{time1} to {time2}"
    else:
        raise ValueError


def new_time(hrs, mins, am_pm):
    #new_hrs = int(hrs) if am_pm == "AM" else int(hrs) + 12 if int(hrs) != 12 else 0
    #ternary operator not working as expected,  gives two error
    if am_pm == "PM":
        if int(hrs) == 12:
            new_hrs = 12
        else:
            new_hrs = int(hrs) + 12
    else:
        if int(hrs) == 12:
            new_hrs = 0
        else:
            new_hrs = int(hrs)
    if mins == None:
        new_mins = "00"
        new_time = f"{new_hrs:02}" + ":" + new_mins
    else:
        new_time = f"{new_hrs:02}" + ":" + mins
    return new_time



if __name__ == "__main__":
    main()
