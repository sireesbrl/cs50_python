camelCase = input("camelCase: ").strip()

print("snake_case: ", end = "")

for i in range(len(camelCase)):
    if camelCase[i].isupper():
        print(f"_{camelCase[i].lower()}", end = "")
    else:
        print(camelCase[i], end = "")
