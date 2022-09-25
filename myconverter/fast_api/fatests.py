import requests
print('начат main')
answer = requests.get("http://127.0.0.1:8001/api/v1/apitesting")
# answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi")
print(f' eto answer one user: {answer.json()}')