import requests

data = {"username":"Otavio","secret": "@admin" ,"info": "cargo","value": "Supervisor"}
response = requests.post("http://127.0.0.1:5000/informations", data=data)

if response.status_code == 200:
    msg = response.json()
    print(msg)
else:
    print((response.status_code))
msg = response.json()
print(msg['empregados'])