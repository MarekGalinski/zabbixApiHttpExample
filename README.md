# Zabbix HTTP Agent items create and get example
### Using OpenWeatherMap API key

The example scripts in Python below show how to create an HTTP Agent item in Zabbix (v4.4 or higher)

#### Before you start

Get an API key from OpenWeatherMap here: https://openweathermap.org/appid

## How to use

Brief manual on how to use following scripts

#### zabbix_setOpenWeatherTemp.py 

This script will create an HTTP Agent agent with JSON preprocessing that will get the current temperature for given city in Kelvin with 30s refresh rate.

You do not have to change code, just set properly your:
- Zabbix URL
- HostId (maybe you will have to change host interface also)
- Zabbix username and password
- OpenWeatherMap API key
- City

#### zabbix_getOpenWeatherTemp.py 

This script will get the current temperature for given city if the HTTP item was created by the script `zabbixsetOpenWeatherTemp.py`

You do not have to change code, just set properly your:
- Zabbix URL
- HostId (maybe you will have to change host interface also)
- Zabbix username and password
- City

#### License notes

Just take it and do whatever you want. Is as is. Will not be different. Or maybe will. Who knows.
