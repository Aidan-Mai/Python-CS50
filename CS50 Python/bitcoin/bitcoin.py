import requests
import json
import sys

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print('Command-line argument is not a number')
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = bitcoin.json()
    mult = (response['bpi']['USD']['rate_float'])
    total = value * mult
    print(f"${total:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit(1)
