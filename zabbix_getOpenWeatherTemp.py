import requests
import json

#ZABBIX SETTINGS
url = "http://0.0.0.0/zabbix/api_jsonrpc.php"
hostid = "00000"

#ZABBIX AUTHENTIFICATION
uname = "Admin"
passw = "zabbix"

#OPENWEATHER SETTING
city = "Bratislava"

## AUTHENTIFICATION
payload = "{\n    \"jsonrpc\": \"2.0\",\n    \"method\": \"user.login\",\n    \"params\": {\n        \"user\": \""+ uname +"\",\n        \"password\": \""+ passw +"\"\n    },\n    \"id\": 1,\n    \"auth\": null\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "5ca33c0f-4c26-4a2d-aedd-178795bc1292"
    }

response = requests.request("POST", url, data=payload, headers=headers)

login_response = json.loads(response.text);
auth = login_response["result"]

payload = "{\n    \"jsonrpc\": \"2.0\",\n    \"method\": \"item.get\",\n    \"params\": {\n        \"output\": \"extend\",\n        \"hostids\": \""+ hostid +"\",\n        \"search\": {\n            \"key_\": \""+ city +"\"\n        },\n        \"sortfield\": \"name\"\n    },\n    \"auth\": \""+ auth +"\",\n    \"id\": 1\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "d103bde0-525e-4ed5-98fe-27842fcac714"
    }

response = requests.request("POST", url, data=payload, headers=headers)

result = json.loads(response.text)
kelvin = result["result"][0]["lastvalue"]
celsius = float(kelvin) -273.15
print("Current weather in", city , round(celsius,2), "Celsius")


