
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
  # print("calling /api/folders")
  conn.request("GET", "/api/folders", payload, headers)
  res = conn.getresponse()
  data = res.read()
  return data.decode("utf-8")

def getUsers():
  conn.request("GET", "/api/org/users", payload, headers)
  res = conn.getresponse()
  data = res.read()
  return (data.decode("utf-8"))

def printUserLogins():
  usersJson = json.loads(getUsers())
  for user in range(len(usersJson)):
    print(user, usersJson[user]["login"])

def printFolderNames():
  foldersJson = json.loads(getFolders())
  for folder in range(len(foldersJson)):
    print(folder, foldersJson[folder]["title"])


printUserLogins()
printFolderNames()

foldersJson = json.loads(getFolders())

print(foldersJson)