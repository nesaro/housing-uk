import requests
from urllib.parse import urlencode
from pprint import pprint
import json

def property_listings(place_name):
    url = "http://api.nestoria.co.uk/api?action=search_listings&encoding=json&place_name={0}&number_of_results=20&price_max=300000".format(place_name)
    response = requests.get(url)
    json_response = response.json()
    pprint(json_response)

if __name__ == '__main__':
    property_listings('east ham station')
