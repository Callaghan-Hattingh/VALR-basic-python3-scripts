#Get - Currency Pairs [3]

import http.client
import json

conn = http.client.HTTPSConnection('api.valr.com')

verb = 'GET'
path = '/v1/public/pairs'
payload = {}
headers = {}

conn.request(verb, path, payload, headers)
res = conn.getresponse()
data = res.read()

#To Pretty print the json data
j_data = json.loads(data) 
print (json.dumps(j_data, sort_keys=True, indent=4))

conn.close() #Close the connetion