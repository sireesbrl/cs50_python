total = {}
while True:
    try:
        item = input().strip().upper()
    except EOFError:
        print()
        break
    else:
        if not item in total:
            total[f"{item}"] = 1
        else:
            total[item] = total[item] + 1



for items in sorted(total):
    print(f"{total[items]} {items}")
