import requests
import sys

try:
    sys.argv[1]
    number = float(sys.argv[1])
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r = r.json()
    value = r['bpi']['USD']["rate_float"]
    amount = number * value
    print(f"${amount:,.4f}")
    
except ValueError:
    sys.exit("Command-line argument is not a number.")
except IndexError:
    sys.exit('Missing command-line argument.')
except requests.RequestException:
    ...
