import requests
response = requests.get('https://freegeoip.app/json/')
data = response.json()
ENTITY_LOCATION = f"{data['city']}, {data['region_name']}, {data['country_name']}"
LATITUDE = data['latitude']
LONGITUDE = data['longitude']
print(ENTITY_LOCATION)
print(LATITUDE)
print(LONGITUDE)

#**Method 2: Using IPAPI (another free IP Geolocation API)**

import requests
response = requests.get('https://ipapi.co/json/')
data = response.json()
ENTITY_LOCATION = f"{data['city']}, {data['region']}, {data['country_name']}"
LATITUDE = data['latitude']
LONGITUDE = data['longitude']
print(ENTITY_LOCATION)
print(LATITUDE)
print(LONGITUDE)

"""Replace `ENTITY_LOCATION` variable in your original script with this automated approach."""
