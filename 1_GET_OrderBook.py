#GET - Order Book [1] 

import http.client
import json

conn = http.client.HTTPSConnection('api.valr.com')

verb = 'GET'
pair = 'BTCZAR' #Change BTCZAR with ETHZAR or XRPZAR
path = '/v1/public/{}/orderbook'.format(pair)
payload = {}
headers = {}

conn.request(verb, path, payload, headers) 
res = conn.getresponse()
data = res.read()

#To Pretty print the json data
j_data = json.loads(data) 
print (json.dumps(j_data, sort_keys=True, indent=4))

conn.close() #Close the connetion