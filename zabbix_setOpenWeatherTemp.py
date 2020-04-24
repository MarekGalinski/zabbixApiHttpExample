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
openWeatherApiKey = "your_openweathermaps_api_key_here"


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

## ADDING HTTP ITEM - TEMPERATURE FROM OPENWEATHERMAP API IN KELVIN FOR CITY
payload = "{\n    \"jsonrpc\": \"2.0\",\n    \"method\": \"item.create\",\n    \"params\": {\n        \"url\": \"https://api.openweathermap.org/data/2.5/weather?appid="+ openWeatherApiKey +"&q="+ city +"\",\n        \"interfaceid\": \"2\",\n        \"type\":\"19\",\n        \"hostid\":\""+ hostid +"\",\n        \"delay\":\"30s\",\n        \"key_\":\"api_weather_"+ city +"\",\n        \"name\":\"Weather in "+ city +"\",\n        \"value_type\":\"0\",\n        \"output_format\":\"1\",\n        \"preprocessing\": [\n            {\n                \"type\": \"12\",\n                \"params\": \"$.body.main.temp\",\n                \"error_handler\": \"1\",\n                \"error_handler_params\": \"\"\n            }\n        ]\n    },\n    \"auth\": \""+ auth +"\",\n    \"id\": 2\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "f05830b5-836d-4d04-b936-4966a9d008a9"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
