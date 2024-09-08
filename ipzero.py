import socket
import requests
import pprint
import json

hostname = input('Masukan Website Tujuan: ')
ip_address = socket.gethostbyname(hostname)

# Construct the request URL
request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)

# Decode and parse the JSON response
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation_dict = json.loads(geolocation)


for k, v in geolocation_dict.items():
    pprint.pprint(f'{k} : {v}')