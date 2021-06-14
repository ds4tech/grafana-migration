
import http.client
import json

conn = http.client.HTTPSConnection("monitoring.ops.sdu-rds.com")

payload = ''
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer eyJrIjoiMFpuTklEU2RabjZNR3ZMYWh0aWNiNDZMNHBOQWZXVWEiLCJuIjoibW9kaWZ5QWNjZXNzIiwiaWQiOjF9'
}

def getFolders():
  print("Hello from a function")
  conn.request("GET", "/api/folders", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))

def getUsers():
  conn.request("GET", "/api/org/users", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))


getFolders()
# getUsers()