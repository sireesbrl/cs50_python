#manages meal time in a day

def main():
    time = input("What time is it? (##:##)(24 hrs or AM/PM): ").lower().strip()
    if "am" in time:
        time = time.replace("am","").strip()
        if 7.0<=convert(time)<=8.0:
             print("breakfast time...")
    elif "pm" in time:
        time = time.replace("pm","").strip()
        if convert(time)>=12.0 or convert(time)<=1.0:
             print("lunch time")
        if 6.0<=convert(time)<=7.0:
             print("dinner time")
    else:
         if 7.0<=convert(time)<=8.0:
             print("breakfast time")
         elif 12.0<=convert(time)<=13.0:
              print("lunch time")
         elif 18.0<=convert(time)<=19.0:
              print("dinner time")


def convert(time):
        time_new = 0.0
        hours, minutes = time.split(":")
        x = float(hours)
        y = float(minutes)
        if 1.0<=x<=24.0 and 0.0<=y<=60.0:
            time_new = x + (1/60)*y
            return time_new

if __name__ == "__main__":
    main()
