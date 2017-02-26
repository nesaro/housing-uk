import requests
from settings import ZOOPLA_API_KEY
from urllib.parse import urlencode
from pprint import pprint
import json

PROPERTY_LISTINGS_URL = 'http://api.zoopla.co.uk/api/v1/property_listings'
def property_listings(area, radius=1):
    url = PROPERTY_LISTINGS_URL + urlencode({'area':area, 'radius':radius})
    response = requests.get(url)
    pprint(response.text)
    json_response = response.json()
    pprint(json_response)

if __name__ == '__main__':
    property_listings('east ham station')
    

