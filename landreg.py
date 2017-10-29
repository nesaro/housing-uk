#https://www.gov.uk/guidance/about-the-price-paid-data
#"{55BDCAE6-6654-521D-E053-6B04A8C0DD7A}","450000","2017-06-30 00:00","DA6 8JQ","S","N","F","3","","HANSOL ROAD","","BEXLEYHEATH","BEXLEY","GREATER LONDON","A","A"

COLUMNS = ('id', 'price', 'datetime', 'postcode', 'property_type', 'new', 'duration', 'PAON', 'SAON', 'Street','Locality','Town','District', 'County', 'PPD')

#property type =    D = Detached, S = Semi-Detached, T = Terraced, F = Flats/Maisonettes, O = Other 

#duration : F = Freehold, L= Leasehold etc.  Note that HM Land Registry does not record leases of 7 years or less in the Price Paid Dataset.

#PPD    Indicates the type of Price Paid transaction.
#A = Standard Price Paid entry, includes single residential property sold for full market value.
#B = Additional Price Paid entry including transfers under a power of sale/repossessions, buy-to-lets (where they can be identified by a Mortgage) and transfers to non-private individuals.

import csv
from pprint import pprint
import datetime

results = []
with open('pp-2017.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        dict_row = dict(zip(COLUMNS,row))
        dict_row['new'] = dict_row['new'] == 'Y'
        dict_row['datetime'] = datetime.datetime.strptime(dict_row['datetime'], '%Y-%m-%d %H:%M').date()
        if dict_row['postcode'].startswith('N1 ') and dict_row['property_type'] == 'F':
            results.append([dict_row[x] for x in ['datetime', 'price', 'postcode', 'PAON', 'SAON']])

pprint(sorted(results, key=lambda x:x[0]))



