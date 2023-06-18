#!/user/bin/env python

import json
from urllib.request import urlopen
import socket


print("Enter IP: ")

input = input()

def domain(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Not Found"

try:
    url = 'https://ipinfo.io/' + input
    response = urlopen(url)
    data = json.load(response)


    ip = data['ip']
    city = data['city']
    region = data['region']
    postal = data['postal']
    country = data['country']
    loc = data['loc']
    org = data['org']
    timezone = data['timezone']

    print("\n")
    print("IP: " + ip)
    print("Domain:", domain(input))
    print("City: " + city)
    print("Region: " + region)
    print("Zip: " + postal)
    print("Country: " + country)
    print("Lat/Long: " + loc)
    print("Company: " + org)
    print("Timezone: " + timezone) 
except:
    print("HTTP Error 404: Not Found")
