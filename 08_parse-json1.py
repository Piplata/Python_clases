# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:18:56 2020

@author: CEC
"""

import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest= "Ibarra"
key = "dyRPvKBZMNyFF8ANGfGjOAxwTUhC4uoK"

url = main_api + urllib.parse.urlencode({"key":key, "from": orig, "to": dest})
json_data = requests.get(url).json()
print(json_data)