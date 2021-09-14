import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "Daniel", "id": 5, "date": "13-09-2021"},
        {"name": "afdasf",
         "id": 7, "date": "21-05-2022"},
        {"name": "mkmkmk", "id": 6, "date": "25-01-2022"},
        {"name": "Daniel Shalom", "id": 1, "date": "13-09-2021"}]


for i in range(len(data)):
    response = requests.put(BASE + "order/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(BASE + "order/13-09-2021")

print(response.json())
