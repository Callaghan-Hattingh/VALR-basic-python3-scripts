#Get - Order Types for a currency pair [5]

import http.client
import json

conn = http.client.HTTPSConnection('api.valr.com')

verb = 'GET'
pair = 'BTCZAR'
path = '/v1/public/{}/ordertypes'.format(pair)
payload = {}
headers = {}

conn.request(verb, path, payload, headers)
res = conn.getresponse()
data = res.read()

#To Pretty print the json data
j_data = json.loads(data) 
print (json.dumps(j_data, sort_keys=True, indent=4))

conn.close() #Close the connetion