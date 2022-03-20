import http.client
import json

conn = http.client.HTTPConnection("127.0.0.1", 9000)
payload = json.dumps({
  "library": "netmiko",
  "connection_args": {
    "device_type": "hp_comware",
    "host": "192.168.56.21",
    "username": "netdevops",
    "password": "NetDevops@01"
  },
  "command": "dis version",
  "args": {
    "use_textfsm": False
  },
  "queue_strategy": "pinned"
})
headers = {
  'x-api-key': '2a84465a-cf38-46b2-9d86-b84Q7d57f288',
  'Content-Type': 'application/json'
}
# conn.request("POST", "/getconfig", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

payload = ''
conn.request("GET", "/task/c24651ea-d4f6-43af-8d42-74918648a1d0", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))