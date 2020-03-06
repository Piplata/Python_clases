# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:58:26 2020

@author: CEC
"""

import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "dyRPvKBZMNyFF8ANGfGjOAxwTUhC4uoK"
while True: 
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key":key, "from": orig, "to": dest})
    print("URL: "+ (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0: 
    print('API Status: ' + str(json_status) + '= A successful route call. \n')