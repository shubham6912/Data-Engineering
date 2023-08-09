import http.client
import array as arr

a = arr.array('i', [15878,15884,15913,16108,16181,16256,16297,16395,16408,16411,16416,16550,16548,16926,17040,17331,17394,17527,17552,17738,17959,18196,18322,18475,18636,18748,18960,19696,19821,20179,20188,20232,20494,20593,20713,20763,21333,21433,22091])
for x in a:
  payload = 'customerId=:cid&action=true&packageId=103&allDevices=true&packageName=Tag%20Management'
  print(x)
  conn = http.client.HTTPSConnection("url")
  payload=payload.replace(":cid",str(x))

  headers = {
   'authority': 'url',
   'accept': '*/*',
   'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
   'authorization': 'Basic <token>',
   }
  conn.request("POST", "url", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))  
