fruits = {"apple":"130", "avocado": "50", "banana":"110",
          "kiwifruit":"90", "pear":"100", "sweet cherries": "100"}

fruit = input("Item: ").lower().strip()

if fruit in fruits:
    print(f"Calories: {fruits[fruit]}")

