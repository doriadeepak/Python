import json
from urllib.request import urlopen

with urlopen("https://open.er-api.com/v6/latest/USD") as response:
    source=response.read()

data=json.loads(source)

# print(json.dumps(data,indent=2))

usd_rates={}

for item in data["rates"]:
    name=item
    rate=data["rates"][item]
    usd_rates[name]=rate

print("USD/EUR: ",float(usd_rates["EUR"]))
print("50 USD = ",50*float(usd_rates["EUR"]),"EUR")
print("USD/INR: ",float(usd_rates["INR"]))
print("50 USD = ",50*float(usd_rates["INR"]),"INR")
