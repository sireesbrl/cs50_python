import requests
import sys

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
elif len(sys.argv) == 2:
    try:
        bit_coin = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)

else:
    rate = r.json()["bpi"]["USD"]["rate_float"]
    print(f"${(rate * bit_coin):,.4f}")



