import requests
response = requests.get("https://api.bitflyer.jp/v1/ticker/")
print(response.json())
