"""
    search.py

    MediaWiki Action API Code Samples
    Demo of `Search` module: Search for a text or title
    MIT license
"""

import requests
import os

cert = 'p:/MyWork/cacert.pem'

S = requests.Session()

URL = "https://www.wikidata.org/w/api.php"

SEARCHTERM = "Beazley"

PARAMS = {
    'action':"query",
    'list':"search",
    'srsearch': SEARCHTERM,
    'format':"json"
}

PARAMS = {
    'action':"opensearch",
    'search':SEARCHTERM,
    'limit': 5,
    'namespace':0,
    'format':"json"
}

PARAMS = {
    'action':'wbsearchentities',
	'search':SEARCHTERM,
	'language':'en',
	'type':'item',
	'format':'json',
    }

R = S.get(url=URL,
          params=PARAMS,
          verify=cert)

DATA = R.json()

print(DATA)
#if DATA['query']['search'][0]['title'] == SEARCHPAGE:
#    print("Your search page '" + SEARCHPAGE + "' exists on English Wikipedia")

## get data
#https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities