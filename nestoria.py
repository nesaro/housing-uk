import requests
from urllib.parse import urlencode
from pprint import pprint
import json

def collection_factory():
    from pymongo import MongoClient
    from pymongo.errors import DuplicateKeyError
    client = MongoClient('localhost', 27017)
    database = client.test_housing_uk
    nestoria_collection = database.nestoria
    try:
        nestoria_collection.create_index('nestoria_index',unique=True)
    except DuplicateKeyError:
        pass
    return nestoria_collection



def attach_nestoria_index(element):
    lister_url = element['lister_url']
    import re
    nestoria_index = re.search('http://www.nestoria.co.uk/detail/(\d+)/.*', lister_url).group(1)
    nestoria_index = nestoria_index.lstrip('0')
    element['nestoria_index'] = nestoria_index

def property_listings(place_name):
    url = "http://api.nestoria.co.uk/api?action=search_listings&encoding=json&place_name={0}&number_of_results=20&price_max=300000".format(place_name)
    response = requests.get(url)
    json_response = response.json()
    return json_response['response']['listings']

def store_listing(listing):
    collection = collection_factory()
    for element in listing:
        attach_nestoria_index(element)
        collection.replace_one({'nestoria_index':element['nestoria_index']}, element, upsert=True)
        pprint(element)


if __name__ == '__main__':
    listings = property_listings('east ham station')
    store_listing(listings)
    collection = collection_factory()
    print(collection.count())

