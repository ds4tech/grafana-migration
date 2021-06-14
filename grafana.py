
import http.client
import json

conn = http.client.HTTPSConnection("monitoring.ops.sdu-rds.com")
payload = ''
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer eyJrIjoiMFpuTklEU2RabjZNR3ZMYWh0aWNiNDZMNHBOQWZXVWEiLCJuIjoibW9kaWZ5QWNjZXNzIiwiaWQiOjF9'
}
conn.request("GET", "/api/folders", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
