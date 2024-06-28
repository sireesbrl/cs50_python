months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
        if 1<=int(month)<=12 and 1<=int(day)<=31:
            break
    except:
        try:
            temp_month, temp_day, year = date.split(" ")
            if not temp_day.endswith(","):
                continue
            else:
                day = temp_day.strip().replace(",", "")
            for i in range(len(months)):
                if temp_month.title() == months[i]:
                    month = i + 1
            if 1<=int(month)<=12 and 1<=int(day)<=31:
                break
        except:
            pass


print(f"{year}-{int(month):02}-{int(day):02}")
