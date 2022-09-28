import requests
print('начат main')
# answer = requests.get("http://127.0.0.1:8001/api/v1/apitesting")
# answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi")
answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi/get_model_object_by_id/efc94832-a392-4d68-b117-f90b5080218d")
print(f' eto answer one user: {answer.json()}')
